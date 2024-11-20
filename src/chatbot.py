from experta import Fact
from .knowledge_base import CarTroubleshootingSystem
from .knowledge_base import CarDiagnosis
from .bayesian_network import create_bayesian_network
import re
from pgmpy.inference import VariableElimination

class CarTroubleshootingChatbot:
    def __init__(self):
        self.engine = CarTroubleshootingSystem()
        self.engine.reset()
        self.bayesian_network = create_bayesian_network()
        
        # Verify that the Bayesian network is correctly initialized
        print("DEBUG - Variables in the Bayesian network:", self.bayesian_network.nodes())
        print("DEBUG - CPDs in the Bayesian network:", [cpd.variable for cpd in self.bayesian_network.get_cpds()])
        
        self.inference = VariableElimination(self.bayesian_network)
        self.current_question = None
        self.evidence = {}
        
    def update_probabilities(self, symptom, value):
        print(f"DEBUG - Updating probabilities for: {symptom} with value: {value}")
        
        # Complete mapping of questions to variables
        symptom_mapping = {
            'Do the Starter spins?': 'Battery',
            'Do the battery read over 12V?': 'Battery',
            'Are the terminals clean?': 'Battery',
            'Spark from coil?': 'Ignition',
            'Check Engine Light On?': 'CheckEngineLight',
            'Do the brakes feel spongy?': 'BrakeSystem',
            'Is the brake pedal firm?': 'BrakePedal',
            'Is the steering loose?': 'SteeringSystem',
            'Is the power steering working?': 'PowerSteering',
            'Is there an electrical failure?': 'ElectricalSystem',
            'Was the Alternator tested OK?': 'Alternator'
        }
        
        # Get the corresponding variable
        bayesian_var = symptom_mapping.get(symptom)
        if bayesian_var:
            # Save the individual response
            self.evidence[symptom] = int(value == 'yes')
            
            # Update the variables of the Bayesian network according to the system
            if bayesian_var == 'Battery':
                problems = self._count_battery_problems()
                self.evidence['Battery'] = 1 if problems >= 2 else 0
            elif bayesian_var in ['BrakeSystem', 'BrakePedal']:
                problems = self._count_brake_problems()
                self.evidence['BrakeFailure'] = 1 if problems >= 1 else 0
            elif bayesian_var in ['SteeringSystem', 'PowerSteering']:
                problems = self._count_steering_problems()
                self.evidence['SteeringIssue'] = 1 if problems >= 1 else 0
            elif bayesian_var in ['ElectricalSystem', 'Alternator']:
                problems = self._count_electrical_problems()
                self.evidence['ElectricalFailure'] = 1 if problems >= 1 else 0
            
            print(f"DEBUG - Current evidence: {self.evidence}")
            
            try:
                prob_failure = self._calculate_system_probability(bayesian_var)
                return prob_failure, bayesian_var
                    
            except Exception as e:
                print(f"DEBUG - Error in probability calculation: {str(e)}")
                print(f"DEBUG - Error type: {type(e)}")
                return None, None
        
        print(f"DEBUG - Variable not found in the mapping: {symptom}")
        return None, None

    def _count_battery_problems(self):
        problems = 0
        if 'Do the Starter spins?' in self.evidence and self.evidence['Do the Starter spins?'] == 0:
            problems += 1
        if 'Do the battery read over 12V?' in self.evidence and self.evidence['Do the battery read over 12V?'] == 0:
            problems += 1
        if 'Are the terminals clean?' in self.evidence and self.evidence['Are the terminals clean?'] == 0:
            problems += 1
        return problems

    def _count_brake_problems(self):
        problems = 0
        if 'Do the brakes feel spongy?' in self.evidence and self.evidence['Do the brakes feel spongy?'] == 1:
            problems += 1
        if 'Is the brake pedal firm?' in self.evidence and self.evidence['Is the brake pedal firm?'] == 0:
            problems += 1
        return problems

    def _count_steering_problems(self):
        problems = 0
        if 'Is the steering loose?' in self.evidence and self.evidence['Is the steering loose?'] == 1:
            problems += 1
        if 'Is the power steering working?' in self.evidence and self.evidence['Is the power steering working?'] == 0:
            problems += 1
        return problems

    def _count_electrical_problems(self):
        problems = 0
        if 'Is there an electrical failure?' in self.evidence and self.evidence['Is there an electrical failure?'] == 1:
            problems += 1
        if 'Was the Alternator tested OK?' in self.evidence and self.evidence['Was the Alternator tested OK?'] == 0:
            problems += 1
        return problems

    def _calculate_system_probability(self, bayesian_var):
        # Create a dictionary of evidence only with the variables of the Bayesian network
        bayesian_evidence = {}
        
        if bayesian_var in ['Battery', 'Ignition']:
            # Only use the Battery variable, not the individual questions
            bayesian_evidence['Battery'] = self.evidence.get('Battery', 0)
            query_result = self.inference.query(['NoStart'], evidence=bayesian_evidence)
            prob_values = query_result.values
            prob_failure = float(prob_values[1])
            problems = self._count_battery_problems()
            
        elif bayesian_var in ['BrakeSystem', 'BrakePedal']:
            bayesian_evidence['BrakeFailure'] = self.evidence.get('BrakeFailure', 0)
            query_result = self.inference.query(['BrakeFailure'], evidence=bayesian_evidence)
            prob_values = query_result.values
            prob_failure = float(prob_values[1])
            problems = self._count_brake_problems()
            
        elif bayesian_var in ['SteeringSystem', 'PowerSteering']:
            bayesian_evidence['SteeringIssue'] = self.evidence.get('SteeringIssue', 0)
            query_result = self.inference.query(['SteeringIssue'], evidence=bayesian_evidence)
            prob_values = query_result.values
            prob_failure = float(prob_values[1])
            problems = self._count_steering_problems()
            
        elif bayesian_var in ['ElectricalSystem', 'Alternator']:
            query_result = self.inference.query(['ElectricalFailure'], evidence=self.evidence)
            prob_values = query_result.values
            prob_failure = float(prob_values[1])
            problems = self._count_electrical_problems()
        
        # Adjust the probability based on the number of problems
        if problems == 1:
            prob_failure = (prob_failure + 0.3) / 2
        elif problems >= 2:
            prob_failure = (prob_failure + 0.7) / 2
            
        return prob_failure

    def diagnose(self, message):
        message = message.lower()
        message = re.sub(r'[^\w\s]', '', message)

        print(f"DEBUG - Received message: {message}")

        if self.current_question:
            print(f"DEBUG - Processing current question: {self.current_question}")
            prob, bayesian_var = self.update_probabilities(self.current_question, message)
            
            # Process the current response before getting the next question
            expected_fact = self.engine.expected_facts.get(self.current_question)
            if expected_fact:
                print(f"DEBUG - Declaring fact: {expected_fact}={message}")
                self.engine.declare(CarDiagnosis(**{expected_fact: message}))
                self.engine.run()
            
            next_question = self.process_questions()
            probability_message = ""
            
            if prob:
                # Get the system name based on the current Bayesian variable
                system_names = {
                    'Battery': 'Battery System',
                    'Ignition': 'Ignition System',
                    'BrakeSystem': 'Brake System',
                    'BrakePedal': 'Brake System',
                    'SteeringSystem': 'Steering System',
                    'PowerSteering': 'Steering System',
                    'ElectricalSystem': 'Electrical System',
                    'Alternator': 'Electrical System'
                }
                system_name = system_names.get(bayesian_var, 'System')
                
                if prob > 0.7:
                    probability_message = f"High probability ({prob:.2f}) of failure in the {system_name}. Immediate inspection recommended.\n"
                elif prob > 0.5:
                    probability_message = f"Moderate to high probability ({prob:.2f}) of failure in the {system_name}.\n"
                elif prob > 0.3:
                    probability_message = f"Some indicators of possible failure ({prob:.2f}) in the {system_name}.\n"
            
            if "Diagnostic:" in next_question:
                print("DEBUG - next_question: ", next_question)
                self.current_question = None
                self.evidence = {}
                return f"{probability_message}. {next_question} \n Diagnosis completed. Is there any other problem you would like to consult?"
            else:
                return f"{probability_message}. {next_question}"

        symptoms = {
            #Respond to starter cranks? -> NO
            'no_start': ["not starting", "no start", "wont start", "won't start", "doesn't start", "does not start", "car won't turn on"],
            #Respond to starter cranks? -> YES
            'car_stall': ["car stall", "car start and stall", "car stops", "the car starts and then stalls"],
            #Respond to clunk or single tick -> YES
            'unusual_noise': ["unusual noise", "strange noise", "weird sound", "clicking noise", "knocking noise", "noise in car"],
            #Respond to clunk or single tick -> NO
            'tick_noise': ["tick noise", "unusual tick noises", "ticks on engine", "ticks", "tick when moving"],
            #Respond to streaming or leak -> YES
            'streaming': ["streaming", "stream", "smoking", "stream from engine"],
            #Respond to streaming or leak -> NO
            'leaking': ["leaking", "leak", "dropping"],

            #New wait of management problems (testing - kef)
            'brakes_problem': ["brakes problems", "brakes", "brake", "dont have brakes", "car doesn't stop"],
            'steering_problems': ["steering problems", "steering", "loose steering", "loose wheel"],
            'electric_problems': ["electric problems", "electric problem", "electric", "electronic", "wire problems"]
        }

        responds = {
            'no': ["no", "negative", "maybe not", "it not"],
            'yes' : ["yes", "affirmative", "obscurse"]
        }

        for symptom, phrases in symptoms.items():
            for phrase in phrases:
                if phrase in message:
                    if symptom == 'no_start':
                        self.engine.reset()
                        self.engine.declare(CarDiagnosis(starter_cranks='no'))
                        self.evidence = {}
                        self.engine.run()
                        return self.process_questions()
                    if symptom == 'car_stall':
                        self.engine.reset()
                        self.engine.declare(CarDiagnosis(starter_cranks='yes'))
                        self.engine.run()
                        return self.process_questions()
                    if symptom == 'unusual_noise':
                        self.engine.reset()
                        self.engine.declare(CarDiagnosis(clunk_or_singletick='yes'))
                        self.engine.run()
                        return self.process_questions()
                    if symptom == 'tick_noise':
                        self.engine.reset()
                        self.engine.declare(CarDiagnosis(clunk_or_singletick='no'))
                        self.engine.run()
                        return self.process_questions()
                    if symptom == 'streaming':
                        self.engine.reset()
                        self.engine.declare(CarDiagnosis(streaming_or_leak='yes'))
                        self.engine.run()
                        return self.process_questions()
                    if symptom == 'leaking':
                        self.engine.reset()
                        self.engine.declare(CarDiagnosis(streaming_or_leak='no'))
                        self.engine.run()
                        return self.process_questions()
                    if symptom == 'brakes_problem':
                        self.engine.reset()
                        self.engine.declare(CarDiagnosis(brakes_failure='yes'))
                        self.engine.run()
                        return self.process_questions()
                    if symptom == 'steering_problems':
                        self.engine.reset()
                        self.engine.declare(CarDiagnosis(steering_problems='yes'))
                        self.engine.run()
                        return self.process_questions()
                    if symptom == 'electric_problems':
                        self.engine.reset()
                        self.engine.declare(CarDiagnosis(electric_problem='yes'))
                        self.engine.run()
                        return self.process_questions()
  
        for respond, phrases in responds.items():
            for phrase in phrases:
                if phrase in message:
                    return self.respond_to_input(message)
        
        return "Sorry, don't understand the problem. Could you describe the symptom in another way?"

    def process_questions(self):
        questions = self.engine.get_questions()
        if questions:
            self.current_question = questions[0]
            return questions.pop(0)
        return "There are no more questions."

    def respond_to_input(self, user_input):
        print(f"DEBUG - Processing response: {user_input}")
        print(f"DEBUG - Current question: {self.current_question}")
        
        if user_input.lower() in ['yes', 'no']:
            prob, bayesian_var = self.update_probabilities(self.current_question, user_input)
            print(f"DEBUG - Calculated probability: {prob}")
            
            # Process the current response
            expected_fact = self.engine.expected_facts.get(self.current_question)
            if expected_fact:
                print(f"DEBUG - Declaring fact: {expected_fact}={user_input}")
                self.engine.declare(CarDiagnosis(**{expected_fact: user_input}))
                self.engine.run()
            
            next_question = self.process_questions()
            
            if next_question != "There are no more questions.":
                probability_message = ""
                if prob and prob > 0.7:
                    probability_message = f"Failure probability: {prob:.2f}\n"
                return f"{probability_message}{next_question}"
            else:
                self.current_question = None
                self.evidence = {}
                return f"Failure probability: {prob:.2f}\nDiagnosis completed. Is there any other problem you would like to consult?"

        return "Please answer only with 'yes' or 'no'."