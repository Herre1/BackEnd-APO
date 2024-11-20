from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

def create_bayesian_network():
    # Definición de la estructura de la red
    model = BayesianNetwork([
        ('Battery', 'NoStart'),
        ('Ignition', 'NoStart'),
        ('NoStart', 'CheckEngineLight'),
        ('BrakeSystem', 'BrakeFailure'),
        ('BrakePedal', 'BrakeFailure'),
        ('SteeringSystem', 'SteeringIssue'),
        ('PowerSteering', 'SteeringIssue'),
        ('ElectricalSystem', 'ElectricalFailure'),
        ('Alternator', 'ElectricalFailure')
    ])

    # CPDs para problemas de arranque (existentes)
    cpd_battery = TabularCPD(variable='Battery', variable_card=2, 
                            values=[[0.8], [0.2]])  # [Funcional, Defectuoso]
    
    cpd_ignition = TabularCPD(variable='Ignition', variable_card=2, 
                             values=[[0.7], [0.3]])  # [Funcional, Defectuoso]
    
    cpd_no_start = TabularCPD(variable='NoStart', variable_card=2,
                             values=[[0.9, 0.6, 0.7, 0.1],
                                    [0.1, 0.4, 0.3, 0.9]],
                             evidence=['Battery', 'Ignition'],
                             evidence_card=[2, 2])

    cpd_check_engine_light = TabularCPD(variable='CheckEngineLight', variable_card=2,
                                       values=[[0.7, 0.2],
                                              [0.3, 0.8]],
                                       evidence=['NoStart'],
                                       evidence_card=[2])

    # CPDs para sistema de frenos
    cpd_brake_system = TabularCPD(variable='BrakeSystem', variable_card=2,
                                 values=[[0.85], [0.15]])  # [Funcional, Defectuoso]

    cpd_brake_pedal = TabularCPD(variable='BrakePedal', variable_card=2,
                                values=[[0.9], [0.1]])  # [Normal, Anormal]

    cpd_brake_failure = TabularCPD(variable='BrakeFailure', variable_card=2,
                                  values=[[0.95, 0.6, 0.7, 0.1],
                                         [0.05, 0.4, 0.3, 0.9]],
                                  evidence=['BrakeSystem', 'BrakePedal'],
                                  evidence_card=[2, 2])

    # CPDs para sistema de dirección
    cpd_steering_system = TabularCPD(variable='SteeringSystem', variable_card=2,
                                    values=[[0.8], [0.2]])  # [Funcional, Defectuoso]

    cpd_power_steering = TabularCPD(variable='PowerSteering', variable_card=2,
                                   values=[[0.9], [0.1]])  # [Funcional, Defectuoso]

    cpd_steering_issue = TabularCPD(variable='SteeringIssue', variable_card=2,
                                   values=[[0.95, 0.4, 0.3, 0.1],
                                          [0.05, 0.6, 0.7, 0.9]],
                                   evidence=['SteeringSystem', 'PowerSteering'],
                                   evidence_card=[2, 2])

    # CPDs para sistema eléctrico
    cpd_electrical_system = TabularCPD(variable='ElectricalSystem', variable_card=2,
                                      values=[[0.85], [0.15]])  # [Funcional, Defectuoso]

    cpd_alternator = TabularCPD(variable='Alternator', variable_card=2,
                               values=[[0.9], [0.1]])  # [Funcional, Defectuoso]

    cpd_electrical_failure = TabularCPD(variable='ElectricalFailure', variable_card=2,
                                       values=[[0.95, 0.3, 0.4, 0.1],
                                              [0.05, 0.7, 0.6, 0.9]],
                                       evidence=['ElectricalSystem', 'Alternator'],
                                       evidence_card=[2, 2])

    # Agregar todos los CPDs al modelo
    model.add_cpds(cpd_battery, cpd_ignition, cpd_no_start, cpd_check_engine_light,
                  cpd_brake_system, cpd_brake_pedal, cpd_brake_failure,
                  cpd_steering_system, cpd_power_steering, cpd_steering_issue,
                  cpd_electrical_system, cpd_alternator, cpd_electrical_failure)

    # Verificar que el modelo sea válido
    model.check_model()

    return model