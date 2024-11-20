from experta import *

class CarDiagnosis(Fact):
    pass

class CarTroubleshootingSystem(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.questions = []
        self.expected_facts = {}

    def get_questions(self):
        return self.questions

    def clear_questions(self):
        self.questions.clear()


    # Starter Problems

    @Rule(CarDiagnosis(start_problem='yes'))
    def start_problem(self):
        message = 'Do the Starter cranks?'
        self.questions.append(message)
        self.expected_facts[message] = 'starter_cranks'

    @Rule(CarDiagnosis(starter_cranks='no'))
    def starter_cranks_no(self):
        message = "Do the Starter spins?"
        self.questions.append(message)
        self.expected_facts[message] = 'starter_spins'
        # self.declare(CarDiagnosis(starter_spins=''))

    @Rule(CarDiagnosis(starter_spins='yes'))
    def starter_spins_yes(self):
        self.questions.append("Diagnostic: Check if Solenoid stuck or not powered. Also check if there are missing teeth on flywheel")

    @Rule(CarDiagnosis(starter_spins='no'))
    def starter_spins_no(self):
        message = "Do the battery read over 12V?"
        self.questions.append(message)
        self.expected_facts[message] = 'battery_over_12v'
        # self.declare(CarDiagnosis(battery_over_12v=''))

    @Rule(CarDiagnosis(battery_over_12v='yes'))
    def battery_over_12v_yes(self):
        message = "Are the terminals clean?"
        self.questions.append(message)
        self.expected_facts[message] = 'cleaned_terminals'
        # self.declare(CarDiagnosis(cleaned_terminals=''))

    @Rule(CarDiagnosis(cleaned_terminals='yes'))
    def cleaned_terminals_yes(self):
        self.questions.append("Diagnostic: With car in park or neutral, use heavy jumper or screwdriver to bypass starter relay solenoid. Test starter")

    @Rule(CarDiagnosis(cleaned_terminals='no'))
    def cleaned_terminals_no(self):
        self.questions.append("Diagnostic: Clean battery terminals and connectors, engine ground")

    @Rule(CarDiagnosis(battery_over_12v='no'))
    def battery_over_12v_no(self):
        self.questions.append("Diagnostic: Jump start or pop start car and check if battery is charging")

    @Rule(CarDiagnosis(starter_cranks='yes'))
    def starter_cranks_yes(self):
        message = "Do the engine fires?"
        self.questions.append(message)
        self.expected_facts[message] = 'engine_fires'
        # self.declare(CarDiagnosis(engine_fires=''))

    @Rule(CarDiagnosis(engine_fires='yes'))
    def engine_fires_yes(self):
        message = "Starts and stalls?"
        self.questions.append(message)
        self.expected_facts[message] = 'starts_and_stalls'
        # self.declare(CarDiagnosis(starts_and_stalls=''))

    @Rule(CarDiagnosis(starts_and_stalls='no'))
    def starts_and_stalls_no(self):
        self.questions.append("Diagnostic: Check ignition timing, fuel problem")

    @Rule(CarDiagnosis(starts_and_stalls='yes'))
    def starts_and_stalls_yes(self):
        message = "Check OBD, blink code?"
        self.questions.append(message)
        self.expected_facts[message] = 'check_obd'
        # self.declare(CarDiagnosis(check_obd=''))

    @Rule(CarDiagnosis(check_obd='yes'))
    def check_obd_yes(self):
        message = "Stall on key release to run?"
        self.questions.append(message)
        self.expected_facts[message] = 'stalls_on_key_release'
        # self.declare(CarDiagnosis(stalls_on_key_release=''))

    @Rule(CarDiagnosis(stalls_on_key_release='yes'))
    def stalls_on_key_release_yes(self):
        self.questions.append("Diagnostic: Ignition run circuit or column key switch failure. Ring out with meter")

    @Rule(CarDiagnosis(stalls_on_key_release='no'))
    def stalls_on_key_release_no(self):
        message = "Stalls in rain?"
        self.questions.append(message)
        self.expected_facts[message] = 'stalls_in_rain'
        # self.declare(CarDiagnosis(stalls_in_rain=''))

    @Rule(CarDiagnosis(stalls_in_rain='yes'))
    def stalls_in_rain_yes(self):
        self.questions.append("Diagnostic: Check for cracked coil, distributor. Check visible electrical arcing running in dark")

    @Rule(CarDiagnosis(stalls_in_rain='no'))
    def stalls_in_rain_no(self):
        message = "Stalls warm?"
        self.questions.append(message)
        self.expected_facts[message] = 'stalls_warm'
        # self.declare(CarDiagnosis(stalls_warm=''))

    @Rule(CarDiagnosis(stalls_warm='yes'))
    def stalls_warm_yes(self):
        self.questions.append("Diagnostic: Adjust idle, blow out fuel filter, check fuel pump output. Check vacuum leak or sensor failure")

    @Rule(CarDiagnosis(stalls_warm='no'))
    def stalls_warm_no(self):
        self.questions.append("Diagnostic: On cold stalling, check for stuck choke, ERG. Check for vacuum leak")

    @Rule(CarDiagnosis(check_obd='no'))
    def check_obd_no(self):
        self.questions.append("Diagnostic: Read OBD or OBD II or Check for blink code access")

    @Rule(CarDiagnosis(engine_fires='no'))
    def engine_fires_no(self):
        message = "Spark to plugs?"
        self.questions.append(message)
        self.expected_facts[message] = 'spark_to_plugs'
        # self.declare(CarDiagnosis(spark_to_plugs=''))

    @Rule(CarDiagnosis(spark_to_plugs='yes'))
    def spark_to_plugs_yes(self):
        message = "Fuel to filter?"
        self.questions.append(message)
        self.expected_facts[message] = 'fuel_to_filter'
        # self.declare(CarDiagnosis(fuel_to_filter=''))

    @Rule(CarDiagnosis(fuel_to_filter='no'))
    def fuel_to_filter_no(self):
        self.questions.append("Diagnostic: Vapor lock, fuel pump, blockage")

    @Rule(CarDiagnosis(fuel_to_filter='yes'))
    def fuel_to_filter_yes(self):
        message = "Fuel injected?"
        self.questions.append(message)
        self.expected_facts[message] = 'fuel_injected'
        # self.declare(CarDiagnosis(fuel_injected=''))

    @Rule(CarDiagnosis(fuel_injected='no'))
    def fuel_injected_no(self):
        self.questions.append("Diagnostic: Try starter spray in crab, throttle open")

    @Rule(CarDiagnosis(fuel_injected='yes'))
    def fuel_injected_yes(self):
        self.questions.append("Diagnostic: Single point, check throttle body. Electronic multipoint, separate disgnostic")

    @Rule(CarDiagnosis(spark_to_plugs='no'))
    def spark_to_plugs_no(self):
        message = "Spark from coil?"
        self.questions.append(message)
        self.expected_facts[message] = 'spark_from_coil'
        # self.declare(CarDiagnosis(spark_from_coil=''))

    @Rule(CarDiagnosis(spark_from_coil='no'))
    def spark_from_coil_no(self):
        message = "12V+ at coil primary?"
        self.questions.append(message)
        self.expected_facts[message] = 'coil_over_12v'
        # self.declare(CarDiagnosis(coil_over_12v=''))

    @Rule(CarDiagnosis(coil_over_12v='no'))
    def coil_over_12v_no(self):
        self.questions.append("Diagnostic: Ignition system wiring, voltage regulator")

    @Rule(CarDiagnosis(coil_over_12v='yes'))
    def coil_over_12v_yes(self):
        self.questions.append("Diagnostic: Test coil for internal short. Check secondary output wire resistance")

    @Rule(CarDiagnosis(spark_from_coil='yes'))
    def spark_from_coil_yes(self):
        message = "Mechanical distributor?"
        self.questions.append(message)
        self.expected_facts[message] = 'mechanical_distributor'
        # self.declare(CarDiagnosis(mechanical_distributor=''))

    @Rule(CarDiagnosis(mechanical_distributor='no'))
    def mechanical_distributor_no(self):
        self.questions.append("Diagnostic: For electronic distribution, see model manual for more detailed diagnostic checks")

    @Rule(CarDiagnosis(mechanical_distributor='yes'))
    def mechanical_distributor_yes(self):
        self.questions.append("Diagnostic: Check condenser, points or magnetic pick-up, rotor, or cap damage")


    # Car makes noises with running engine

    @Rule(CarDiagnosis(clunk_or_singletick='yes'))
    def clunk_or_singletick_yes(self):
        message = "Noise on bumps only?"
        self.questions.append(message)
        self.expected_facts[message] = 'noise_on_bumps'

    @Rule(CarDiagnosis(noise_on_bumps='yes'))
    def noise_on_bumps_yes(self):
        self.questions.append("Diagnostic: Check struts, shocks, springs, frame welds")

    @Rule(CarDiagnosis(noise_on_bumps='no'))
    def noise_on_bumps_no(self):
        self.questions.append("Diagnostic: Check ball joints, brakes, rack and tie rod ends, motor mounts")    

    @Rule(CarDiagnosis(clunk_or_singletick='no'))
    def clunk_or_singletick_no(self):
        message = "Only ticks when moving?"
        self.questions.append(message)
        self.expected_facts[message] = 'ticks_moving'

    @Rule(CarDiagnosis(ticks_moving='no'))
    def ticks_moving_no(self):
        message = "Preliminary diagnostic: Try to localize tick with hearing tube or long screwdriver. Now respond, Do you hear only ticks when cold?"
        self.questions.append(message)
        self.expected_facts[message] = 'ticks_on_cold'

    @Rule(CarDiagnosis(ticks_on_cold='yes'))
    def ticks_on_cold_yes(self):
        self.questions.append("Diagnostic: Check exhaust pipe forward of catalytic converter for leaks. Listen for lifter rap on valve cover")

    @Rule(CarDiagnosis(ticks_on_cold='no'))
    def ticks_on_cold_no(self):
        message = "Windshield wipers, radio off?"
        self.questions.append(message)
        self.expected_facts[message] = 'windshield_or_radio'

    @Rule(CarDiagnosis(windshield_or_radio='no'))
    def windshield_or_radio_no(self):
        self.questions.append("Diagnostic: Always check the silly stuff...")

    @Rule(CarDiagnosis(windshield_or_radio='yes'))
    def windshield_or_radio(self):
        self.questions.append("Diagnostic: Look for pulley wobble, inspect belts. Check for exhaust manifold leak. Get somebody with better hearing to help you localize where it's coming from on the engine")

    @Rule(CarDiagnosis(ticks_moving='yes'))
    def ticks_moving_yes(self):
        message = "Ticks rolling in neutral?"
        self.questions.append(message)
        self.expected_facts[message] = 'ticks_on_neutral'
    
    @Rule(CarDiagnosis(ticks_on_neutral='no'))
    def ticks_on_neutral_no(self):
        message = "Ticks only in reverse?"
        self.questions.append(message)
        self.expected_facts[message] = 'ticks_on_reverse'

    @Rule(CarDiagnosis(ticks_on_reverse='no'))
    def ticks_on_reverse_no(self):
        self.questions.append("Diagnostic: Possible transmission tick. Check transmission fluid filter")
    
    @Rule(CarDiagnosis(ticks_on_reverse='yes'))
    def ticks_on_reverse_yes(self):
        self.questions.append("Diagnostic: Possible rear brake adjuster, make sure parking brake fully released")

    @Rule(CarDiagnosis(ticks_on_neutral='yes'))
    def ticks_on_neutral_yes(self):
        message = "Frequency drops on shifts?"
        self.questions.append(message)
        self.expected_facts[message] = 'drop_on_shifts'

    @Rule(CarDiagnosis(drop_on_shifts='yes'))
    def drop_on_shifts_yes(self):
        self.declare(CarDiagnosis(ticks_moving='no'))

    @Rule(CarDiagnosis(drop_on_shifts='no'))
    def drop_on_shifts_no(self):
        message = "Only ticks in turns, curves?"
        self.questions.append(message)
        self.expected_facts[message] = 'ticks_on_curves'

    @Rule(CarDiagnosis(ticks_on_curves='yes'))
    def ticks_on_curves_yes(self):
        self.questions.append("Diagnostic: CV joint going or tire too big for wheel well")

    @Rule(CarDiagnosis(ticks_on_curves='no'))
    def ticks_on_curves_no(self):
        message = "Preliminary diagnostic: Tick related to wheel rotation. Now respond, Just changed tires?"
        self.questions.append(message)
        self.expected_facts[message] = 'changed_tires'

    @Rule(CarDiagnosis(changed_tires='yes'))
    def changed_tires_yes(self):
        self.questions.append("Diagnostic: STOP DRIVING NOW! Make sure the wheel lugs were tightened")

    @Rule(CarDiagnosis(changed_tires='no'))
    def changed_tires_no(self):
        message = "Removed hubcaps?"
        self.questions.append(message)
        self.expected_facts[message] = 'removed_hubcaps'

    @Rule(CarDiagnosis(removed_hubcaps='no'))
    def removed_hubcaps_no(self):
        self.questions.append("Diagnostic: Remove hubcaps before proceeding. Loose wire retainer, pebbles can tick")

    @Rule(CarDiagnosis(removed_hubcaps='yes'))
    def removed_hubcaps_yes(self):
        message = "Inspect tire treads?"
        self.questions.append(message)
        self.expected_facts[message] = 'inspect_tire_treads'

    @Rule(CarDiagnosis(inspect_tire_treads='no'))
    def inspect_tire_treads_no(self):
        self.questions.append("Diagnostic: Check for nails or stones embedded in tire tread")

    @Rule(CarDiagnosis(inspect_tire_treads='yes'))
    def inspect_tire_treads_yes(self):
        message = "Ticks only slow speed?"
        self.questions.append(message)
        self.expected_facts[message] = 'ticks_on_lowspeed'

    @Rule(CarDiagnosis(ticks_on_lowspeed='yes'))
    def ticks_on_lowspeed_yes(self):
        self.questions.append("Diagnostic: Check bolted wheel covers")

    @Rule(CarDiagnosis(ticks_on_lowspeed='no'))
    def ticks_on_lowspeed_no(self):
        self.questions.append("Diagnostic: Likely brake pads ticking on warped rotor, also check axles for rubbing")


    # Car engine overheating and antifreeze leaks

    @Rule(CarDiagnosis(streaming_or_leak='no'))
    def streaming_or_leak_no(self):
        message = "Smell antifreeze?"
        self.questions.append(message)
        self.expected_facts[message] = 'smell_antifreeze'

    @Rule(CarDiagnosis(smell_antifreeze='yes'))
    def smell_antifreeze_yes(self):
        self.questions.append("Diagnostic: It's a leak, you jus haven't found it yet")
    
    @Rule(CarDiagnosis(smell_antifreeze='no'))
    def smell_antifreeze_no(self):
        message = "Needle gauge?"
        self.questions.append(message)
        self.expected_facts[message] = 'needle_gauge'

    @Rule(CarDiagnosis(needle_gauge='no'))
    def needle_gauge_no(self):
        message = "First check owners manual for special light behavior. Now respond, Antifreeze level good?"
        self.questions.append(message)
        self.expected_facts[message] = 'antifreeze_level_good'

    @Rule(CarDiagnosis(antifreeze_level_good='no'))
    def antifreeze_level_good_no(self):
        self.questions.append("Diagnostic: Make-up with 50/50, but watch out!")
    
    @Rule(CarDiagnosis(needle_gauge='yes'))
    def needle_gauge_yes(self):
        message = "Returns to normal?"
        self.questions.append(message)
        self.expected_facts[message] = 'ng_return_normal'

    @Rule(CarDiagnosis(ng_return_normal='yes'))
    def ng_return_normal_yes(self):
        self.questions.append("Diagnostic: Sticking, air-locked, or wrong temperature thermostat")

    @Rule(CarDiagnosis(ng_return_normal='no'))
    def ng_return_normal_no(self):
        self.declare(CarDiagnosis(needle_gauge='no'))

    @Rule(CarDiagnosis(antifreeze_level_good='yes'))
    def antifreeze_level_good_yes(self):
        message = "Fan operate?"
        self.questions.append(message)
        self.expected_facts[message] = 'fan_operate'
    
    @Rule(CarDiagnosis(fan_operate='no'))
    def fan_operate_no(self):
        self.questions.append("Diagnostic: Test fan motor with direct connection, check for fan fuse, replace temperature sensor")

    @Rule(CarDiagnosis(fan_operate='yes'))
    def fan_operate_yes(self):
        message = "Flow good?"
        self.questions.append(message)
        self.expected_facts[message] = 'flow_good'

    @Rule(CarDiagnosis(flow_good='no'))
    def flow_good_no(self):
        self.questions.append("Diagnostic: Pump failure or blockage")

    @Rule(CarDiagnosis(flow_good='yes'))
    def flow_good_yes(self):
        message = "Flushed engine?"
        self.questions.append(message)
        self.expected_facts[message] = 'flushed_engine'

    @Rule(CarDiagnosis(flushed_engine='no'))
    def flushed_engine_no(self):
        self.questions.append("Diagnostic: Flush engine with kit, cleaning solution and garden hose, fill with new 50/50 antifreeze")

    @Rule(CarDiagnosis(flushed_engine='yes'))
    def flushed_engine_yes(self):
        message = "Checked thermostat?"
        self.questions.append(message)
        self.expected_facts[message] = 'check_termostat'

    @Rule(CarDiagnosis(check_termostat='no'))
    def check_termostat_no(self):
        self.questions.append("Diagnostic: Throw the thermostat in boiling water and see if it opens. Or just replace it")
    
    @Rule(CarDiagnosis(check_termostat='yes'))
    def check_termostat_yes(self):
        message = "Checked timing?"
        self.questions.append(message)
        self.expected_facts[message] = 'check_timing'

    @Rule(CarDiagnosis(check_timing='yes'))
    def check_timing_yes(self):
        self.questions.append("Diagnostic: If occasional overheating, may be overdriving. Otherwise, suspect improper thermostat installation")
    
    @Rule(CarDiagnosis(check_timing='no'))
    def check_timing_no(self):
        self.questions.append("Diagnostic: Improper ignition timing can lead to overheating")

    @Rule(CarDiagnosis(streaming_or_leak='yes'))
    def streaming_or_leak_yes(self):
        message = "Cap steaming?"
        self.questions.append(message)
        self.expected_facts[message] = 'cap_steaming'

    @Rule(CarDiagnosis(cap_steaming='yes'))
    def cap_steaming_yes(self):
        self.questions.append("Diagnostic: Pressure release working as intended. Check antifreeze level on overflow")

    @Rule(CarDiagnosis(cap_steaming='no'))
    def cap_steaming_no(self):
        message = "Overflow dripping?"
        self.questions.append(message)
        self.expected_facts[message] = 'overflow_dripping'

    @Rule(CarDiagnosis(overflow_dripping='yes'))
    def overflow_dripping_yes(self):
        self.questions.append("Diagnostic: Best place for a drip, but indicates engine too hot or cooling system overfilled")

    @Rule(CarDiagnosis(overflow_dripping='no'))
    def overflow_dripping_no(self):
        message = "Radiator leaking?"
        self.questions.append(message)
        self.expected_facts[message] = 'radiator_leak'

    @Rule(CarDiagnosis(radiator_leak='yes'))
    def radiator_leak_yes(self):
        self.questions.append("Diagnostic: Problem even if overheated. Try stop-leak product or repair or replace radiator")
    
    @Rule(CarDiagnosis(radiator_leak='no'))
    def radiator_leak_no(self):
        message = "Hose leak?"
        self.questions.append(message)
        self.expected_facts[message] = 'hose_leak'

    @Rule(CarDiagnosis(hose_leak='yes'))
    def hose_leak_yes(self):
        self.questions.append("Replace hose or shorten and reclamp if leak is under clamp")

    @Rule(CarDiagnosis(hose_leak='no'))
    def hose_leak_no(self):
        message = "Engine leak?"
        self.questions.append(message)
        self.expected_facts[message] = 'engine_leak'

    @Rule(CarDiagnosis(engine_leak='no'))
    def engine_leak_no(self):
        message = "Heater core leak?"
        self.questions.append(message)
        self.expected_facts[message] = 'heatercore_leak'

    @Rule(CarDiagnosis(heatercore_leak='no'))
    def heatercore_leak_no(self):
        self.declare(CarDiagnosis(antifreeze_level_good='yes'))

    @Rule(CarDiagnosis(heatercore_leak='yes'))
    def heatercore_leak_yes(self):
        self.questions.append("Diagnostic: Heater core hoses, pressure test core, repair or replace")

    @Rule(CarDiagnosis(engine_leak='yes'))
    def engine_leak_yes(self):
        message = "Water pump?"
        self.questions.append(message)
        self.expected_facts[message] = 'water_pump'

    @Rule(CarDiagnosis(water_pump='yes'))
    def water_pump_yes(self):
        self.questions.append("Diagnostic: Leak at water pump almost always means water pump failure")
    
    @Rule(CarDiagnosis(water_pump='no'))
    def water_pump_no(self):
        self.questions.append("Diagnostic: Remove leaking part and installing with new gasket")


    # Brakes failure and brake fluid leaks

    @Rule(CarDiagnosis(brakes_failure='yes'))
    def brakes_failure(self):
        message = "Do the brakes stop the car?"
        self.questions.append(message)
        self.expected_facts[message] = 'brakes_stop_car'

    @Rule(CarDiagnosis(brakes_stop_car='no'))
    def brakes_stop_car_no(self):
        message = "Is the pedal to the floor?"
        self.questions.append(message)
        self.expected_facts[message] = 'pedal_to_floor'

    @Rule(CarDiagnosis(pedal_to_floor='yes'))
    def pedal_to_floor_yes(self):
        message = "Is the brake fluid level OK?"
        self.questions.append(message)
        self.expected_facts[message] = 'brake_fluid_ok'

    @Rule(CarDiagnosis(brake_fluid_ok='yes'))
    def brake_fluid_ok_yes(self):
        message = "Is the brake warning light on?"
        self.questions.append(message)
        self.expected_facts[message] = 'brake_warning_light'

    @Rule(CarDiagnosis(brake_warning_light='yes'))
    def brake_warning_light_yes(self):
        self.questions.append("Diagnostic: If parking brake is released, check the service manual for power booster problem or anti-lock failure.")

    @Rule(CarDiagnosis(brake_warning_light='no'))
    def brake_warning_light_no(self):
        self.questions.append("Diagnostic: Likely power assist related. See the service manual.")

    @Rule(CarDiagnosis(brake_fluid_ok='no'))
    def brake_fluid_ok_no(self):
        self.questions.append("Diagnostic: Fill to the line. If brakes are soft, bleed the lines following the order in the service manual.")

    @Rule(CarDiagnosis(pedal_to_floor='no'))
    def pedal_to_floor_no(self):
        self.questions.append("Diagnostic: Check for pedal linkage binding, glazed or frozen calipers, pinched lines, or booster failure.")

    @Rule(CarDiagnosis(brakes_stop_car='yes'))
    def brakes_stop_car_yes(self):
        message = "Is there a parking brake failure?"
        self.questions.append(message)
        self.expected_facts[message] = 'parking_brake_failure'

    @Rule(CarDiagnosis(parking_brake_failure='yes'))
    def parking_brake_failure_yes(self):
        message = "Are the rear wheels locked?"
        self.questions.append(message)
        self.expected_facts[message] = 'rear_wheel_locked'

    @Rule(CarDiagnosis(rear_wheel_locked='yes'))
    def rear_wheel_locked_yes(self):
        self.questions.append("Diagnostic: Spring return failure or cable rusted/bound.")

    @Rule(CarDiagnosis(rear_wheel_locked='no'))
    def rear_wheel_locked_no(self):
        message = "Does the parking brake ratchet without force?"
        self.questions.append(message)
        self.expected_facts[message] = 'ratchets_without_force'

    @Rule(CarDiagnosis(ratchets_without_force='yes'))
    def ratchets_without_force_yes(self):
        self.questions.append("Diagnostic: Cable stretched, broken, or frozen adjuster.")

    @Rule(CarDiagnosis(ratchets_without_force='no'))
    def ratchets_without_force_no(self):
        self.questions.append("Diagnostic: Shoes worn out, glazed, or fluid in drums.")

    @Rule(CarDiagnosis(parking_brake_failure='no'))
    def parking_brake_failure_no(self):
        message = "Do the wheels drag too much?"
        self.questions.append(message)
        self.expected_facts[message] = 'wheels_drag'

    @Rule(CarDiagnosis(wheels_drag='yes'))
    def wheels_drag_yes(self):
        self.questions.append("Diagnostic: Stuck piston, hydraulic lock, over-adjusted drum shoes, or warped rotor.")

    @Rule(CarDiagnosis(wheels_drag='no'))
    def wheels_drag_no(self):
        message = "Do you need to mash the brakes?"
        self.questions.append(message)
        self.expected_facts[message] = 'mash_brakes'

    @Rule(CarDiagnosis(mash_brakes='yes'))
    def mash_brakes_yes(self):
        message = "Does it happen only after turning?"
        self.questions.append(message)
        self.expected_facts[message] = 'after_turning'

    @Rule(CarDiagnosis(after_turning='yes'))
    def after_turning_yes(self):
        self.questions.append("Diagnostic: Front wheel bearings worn, axle nut loose, or wheel lugs loose.")

    @Rule(CarDiagnosis(after_turning='no'))
    def after_turning_no(self):
        self.questions.append("Diagnostic: Air in the system or fluid leak.")

    @Rule(CarDiagnosis(mash_brakes='no'))
    def mash_brakes_no(self):
        message = "Are the brakes making noises?"
        self.questions.append(message)
        self.expected_facts[message] = 'making_noises'

    @Rule(CarDiagnosis(making_noises='yes'))
    def making_noises_yes(self):
        message = "Are the noises squealing?"
        self.questions.append(message)
        self.expected_facts[message] = 'squealing'

    @Rule(CarDiagnosis(squealing='yes'))
    def squealing_yes(self):
        self.questions.append("Diagnostic: Check pads and shoes for wear, or for foreign objects.")

    @Rule(CarDiagnosis(squealing='no'))
    def squealing_no(self):
        message = "Are there clunks?"
        self.questions.append(message)
        self.expected_facts[message] = 'clunks'

    @Rule(CarDiagnosis(clunks='yes'))
    def clunks_yes(self):
        self.questions.append("Diagnostic: Caliper bolt loose or suspension problem.")

    @Rule(CarDiagnosis(clunks='no'))
    def clunks_no(self):
        message = "Is there scraping or grinding?"
        self.questions.append(message)
        self.expected_facts[message] = 'scraping_or_grinding'

    @Rule(CarDiagnosis(scraping_or_grinding='yes'))
    def scraping_or_grinding_yes(self):
        self.questions.append("Diagnostic: Broken pad or shoe facing, or excessive wear.")

    @Rule(CarDiagnosis(scraping_or_grinding='no'))
    def scraping_or_grinding_no(self):
        message = "Are there rattles?"
        self.questions.append(message)
        self.expected_facts[message] = 'rattles'

    @Rule(CarDiagnosis(rattles='yes'))
    def rattles_yes(self):
        self.questions.append("Diagnostic: Anti-rattle clips on disc pads missing or installed wrong.")

    @Rule(CarDiagnosis(rattles='no'))
    def rattles_no(self):
        self.questions.append("Diagnostic: Chirps and ticks that increase with speed due to rotor warp or run-out.")

    @Rule(CarDiagnosis(making_noises='no'))
    def making_noises_no(self):
        message = "Do the brakes pull to one side?"
        self.questions.append(message)
        self.expected_facts[message] = 'brakes_pull'

    @Rule(CarDiagnosis(brakes_pull='yes'))
    def brakes_pull_yes(self):
        self.questions.append("Diagnostic: Front brake issue, stuck or cocked piston, air or crimp in line, or master cylinder problem.")

    @Rule(CarDiagnosis(brakes_pull='no'))
    def brakes_pull_no(self):
        message = "Are the brakes jerky or pulsing?"
        self.questions.append(message)
        self.expected_facts[message] = 'jerky_or_pulsing'

    @Rule(CarDiagnosis(jerky_or_pulsing='yes'))
    def jerky_or_pulsing_yes(self):
        self.questions.append("Diagnostic: Anti-lock brake issue or deformed drum/rotor (test with parking brake).")

    @Rule(CarDiagnosis(jerky_or_pulsing='no'))
    def jerky_or_pulsing_no(self):
        message = "Is braking hard?"
        self.questions.append(message)
        self.expected_facts[message] = 'hard_braking'

    @Rule(CarDiagnosis(hard_braking='yes'))
    def hard_braking_yes(self):
        self.questions.append("Diagnostic: Worn pads/shoes, bound piston, or power boost problem.")

    @Rule(CarDiagnosis(hard_braking='no'))
    def hard_braking_no(self):
        self.questions.append("If brake warning light on and parking brake is released, see service manual for codes.")


    # Steering problems

    @Rule(CarDiagnosis(steering_problems='yes'))
    def steering_problems(self):
        message = "Loose steering or wheel?"
        self.questions.append(message)
        self.expected_facts[message] = 'loose_steering'

    @Rule(CarDiagnosis(loose_steering='yes'))
    def loose_steering_yes(self):
        message = "Are the lug nuts loose?"
        self.questions.append(message)
        self.expected_facts[message] = 'lug_nuts_loose'

    @Rule(CarDiagnosis(lug_nuts_loose='yes'))
    def lug_nuts_loose_yes(self):
        self.questions.append("Diagnostic: Tighten lug nuts, make sure not cross-threaded.")

    @Rule(CarDiagnosis(lug_nuts_loose='no'))
    def lug_nuts_loose_no(self):
        message = "Is the axle nut loose?"
        self.questions.append(message)
        self.expected_facts[message] = 'axle_nut_loose'

    @Rule(CarDiagnosis(axle_nut_loose='yes'))
    def axle_nut_loose_yes(self):
        self.questions.append("Diagnostic: Check bearing, torque nut, install cotter pin and lock.")

    @Rule(CarDiagnosis(axle_nut_loose='no'))
    def axle_nut_loose_no(self):
        message = "Is the strut or spring bad?"
        self.questions.append(message)
        self.expected_facts[message] = 'strut_or_spring_bad'

    @Rule(CarDiagnosis(strut_or_spring_bad='yes'))
    def strut_or_spring_bad_yes(self):
        self.questions.append("Diagnostic: Replace strut, spring or retainers as needed and realign.")

    @Rule(CarDiagnosis(strut_or_spring_bad='no'))
    def strut_or_spring_bad_no(self):
        message = "Is the lower ball joint bad?"
        self.questions.append(message)
        self.expected_facts[message] = 'lower_ball_joint_bad'

    @Rule(CarDiagnosis(lower_ball_joint_bad='yes'))
    def lower_ball_joint_bad_yes(self):
        self.questions.append("Diagnostic: Replace ball joint.")

    @Rule(CarDiagnosis(lower_ball_joint_bad='no'))
    def lower_ball_joint_bad_no(self):
        message = "Is the tie-rod loose?"
        self.questions.append(message)
        self.expected_facts[message] = 'tie_rod_loose'

    @Rule(CarDiagnosis(tie_rod_loose='yes'))
    def tie_rod_loose_yes(self):
        self.questions.append("Diagnostic: Loose at tie-rod joint with steering knuckle, mark position for alignment and replace. If not, inner tie failed or rack problem.")

    @Rule(CarDiagnosis(tie_rod_loose='no'))
    def tie_rod_loose_no(self):
        message = "Is the steering coupling tight?"
        self.questions.append(message)
        self.expected_facts[message] = 'steering_coupling_tight'

    @Rule(CarDiagnosis(steering_coupling_tight='yes'))
    def steering_coupling_tight_yes(self):
        message = "Is the rack mounting loose?"
        self.questions.append(message)
        self.expected_facts[message] = 'rack_mounting_loose'

    @Rule(CarDiagnosis(rack_mounting_loose='yes'))
    def rack_mounting_loose_yes(self):
        self.questions.append("Diagnostic: Tighten or replace all rack mounting bolts, check cross-member mounting, attachments to lower control arms, swaybar.")

    @Rule(CarDiagnosis(rack_mounting_loose='no'))
    def rack_mounting_loose_no(self):
        self.questions.append("Diagnostic: Pump problems, including low fluid if jerky. Rack or pump failure.")

    @Rule(CarDiagnosis(steering_coupling_tight='no'))
    def steering_coupling_tight_no(self):
        self.questions.append("Diagnostic: Repair coupling.")

    @Rule(CarDiagnosis(loose_steering='no'))
    def loose_steering_no(self):
        message = "Does the steering pull?"
        self.questions.append(message)
        self.expected_facts[message] = 'steering_pulls'

    @Rule(CarDiagnosis(steering_pulls='yes'))
    def steering_pulls_yes(self):
        message = "Is there impact damage?"
        self.questions.append(message)
        self.expected_facts[message] = 'impact_damage'

    @Rule(CarDiagnosis(impact_damage='yes'))
    def impact_damage_yes(self):
        self.questions.append("Diagnostic: If the wheel pulls following hitting a curb, pothole or anything else, a bent part is likely.")

    @Rule(CarDiagnosis(impact_damage='no'))
    def impact_damage_no(self):
        message = "Is there uneven tire wear?"
        self.questions.append(message)
        self.expected_facts[message] = 'uneven_tire_wear'

    @Rule(CarDiagnosis(uneven_tire_wear='yes'))
    def uneven_tire_wear_yes(self):
        self.questions.append("Diagnostic: Toe or camber adjustment.")

    @Rule(CarDiagnosis(uneven_tire_wear='no'))
    def uneven_tire_wear_no(self):
        self.questions.append("Diagnostic: Re-check alignment, possible rack or suspension problem.")

    @Rule(CarDiagnosis(steering_pulls='no'))
    def steering_pulls_no(self):
        message = "Is the steering hard?"
        self.questions.append(message)
        self.expected_facts[message] = 'steering_hard'

    @Rule(CarDiagnosis(steering_hard='yes'))
    def steering_hard_yes(self):
        self.questions.append("Diagnostic: Check power steering pump, belt, tire inflation.")

    @Rule(CarDiagnosis(steering_hard='no'))
    def steering_hard_no(self):
        message = "Is the steering noisy?"
        self.questions.append(message)
        self.expected_facts[message] = 'steering_noisy'

    @Rule(CarDiagnosis(steering_noisy='yes'))
    def steering_noisy_yes(self):
        self.questions.append("Diagnostic: All power steering makes some noise, but check pump.")

    @Rule(CarDiagnosis(steering_noisy='no'))
    def steering_noisy_no(self):
        message = "Is there a power steering leak?"
        self.questions.append(message)
        self.expected_facts[message] = 'power_steering_leak'

    @Rule(CarDiagnosis(power_steering_leak='yes'))
    def power_steering_leak_yes(self):
        self.questions.append("Diagnostic: Check pump, lines, rack seals. Replace or rebuild as necessary.")

    @Rule(CarDiagnosis(power_steering_leak='no'))
    def power_steering_leak_no(self):
        message = "Is there vibration at speed?"
        self.questions.append(message)
        self.expected_facts[message] = 'vibration_at_speed'

    @Rule(CarDiagnosis(vibration_at_speed='yes'))
    def vibration_at_speed_yes(self):
        message = "Does it improve on tire rotation?"
        self.questions.append(message)
        self.expected_facts[message] = 'improves_on_tire_rotation'

    @Rule(CarDiagnosis(improves_on_tire_rotation='yes'))
    def improves_on_tire_rotation_yes(self):
        message = "Is there tire damage or a bent rim?"
        self.questions.append(message)
        self.expected_facts[message] = 'tire_damage_or_bent_rim'

    @Rule(CarDiagnosis(tire_damage_or_bent_rim='yes'))
    def tire_damage_or_bent_rim_yes(self):
        self.questions.append("Diagnostic: If visual inspection shows tire damage or bent rim, replace.")

    @Rule(CarDiagnosis(tire_damage_or_bent_rim='no'))
    def tire_damage_or_bent_rim_no(self):
        self.questions.append("Diagnostic: Rebalance tires.")

    @Rule(CarDiagnosis(improves_on_tire_rotation='no'))
    def improves_on_tire_rotation_no(self):
        message = "Is the CV joint bad?"
        self.questions.append(message)
        self.expected_facts[message] = 'cv_joint_bad'

    @Rule(CarDiagnosis(cv_joint_bad='yes'))
    def cv_joint_bad_yes(self):
        self.questions.append("Diagnostic: Replace or rebuild CV joint.")

    @Rule(CarDiagnosis(cv_joint_bad='no'))
    def cv_joint_bad_no(self):
        self.questions.append("Diagnostic: Check if axle is bent; otherwise, go through loose steering checks.")

    @Rule(CarDiagnosis(vibration_at_speed='no'))
    def vibration_at_speed_no(self):
        self.questions.append("Diagnostic: Vibration when the car isn't moving is engine or transmission/transaxle related.")

    
    #Electrical problems

    @Rule(CarDiagnosis(electric_problem='yes'))
    def electric_problem_yes(self):
        message = "Is there an open circuit with key on 'run'?"
        self.questions.append(message)
        self.expected_facts[message] = 'open_circuit_on_run'

    @Rule(CarDiagnosis(open_circuit_on_run='yes'))
    def open_circuit_on_run_yes(self):
        message = "Is the fusible link blown?"
        self.questions.append(message)
        self.expected_facts[message] = 'fusible_link_blown'

    @Rule(CarDiagnosis(fusible_link_blown='yes'))
    def fusible_link_blown_yes(self):
        message = "Is there a short after the blown link?"
        self.questions.append(message)
        self.expected_facts[message] = 'short_after_blown_link'

    @Rule(CarDiagnosis(short_after_blown_link='yes'))
    def short_after_blown_link_yes(self):
        message = "Preliminary diagnostic: Check for short between ground and run circuit through next connector. Now respond, Is the problem a short circuit?"
        self.questions.append(message)
        self.expected_facts[message] = 'short_circuit'

    @Rule(CarDiagnosis(short_circuit='yes'))
    def short_circuit_yes(self):
        self.questions.append("Diagnostic: Locate the short by visual inspection and replace wire, relay or divice")

    @Rule(CarDiagnosis(short_circuit='no'))
    def short_circuit_no(self):
        self.declare(CarDiagnosis(short_after_blown_link='yes'))

    @Rule(CarDiagnosis(short_after_blown_link='no'))
    def short_after_blown_link_no(self):
        self.questions.append("Diagnostic: Replace with new fusible link rated same or lower.")

    @Rule(CarDiagnosis(fusible_link_blown='no'))
    def fusible_link_blown_no(self):
        message = "Is the ignition switch open?"
        self.questions.append(message)
        self.expected_facts[message] = 'ignition_switch_open'

    @Rule(CarDiagnosis(ignition_switch_open='yes'))
    def ignition_switch_open_yes(self):
        self.questions.append("Diagnostic: Replace or bypass ignition switch.")

    @Rule(CarDiagnosis(ignition_switch_open='no'))
    def ignition_switch_open_no(self):
        message = "Is the battery connector good?"
        self.questions.append(message)
        self.expected_facts[message] = 'battery_connector_good'

    @Rule(CarDiagnosis(battery_connector_good='yes'))
    def battery_connector_good_yes(self):
        message = "Preliminary diagnostic: Check for open between positive and run circuit through next connector. Now respond. Is there an open circuit?"
        self.questions.append(message)
        self.expected_facts[message] = 'open_circuit'

    @Rule(CarDiagnosis(open_circuit='yes'))
    def open_circuit_yes(self):
        self.questions.append("Diagnostic: Locate the open (break) by visual inspection and replace wire, relay or device.")

    @Rule(CarDiagnosis(open_circuit='no'))
    def open_circuit_no(self):
        self.declare(CarDiagnosis(battery_connector_good='yes'))

    @Rule(CarDiagnosis(battery_connector_good='no'))
    def battery_connector_good_no(self):
        self.questions.append("Diagnostic: Laugh, clean or replace.")

    @Rule(CarDiagnosis(open_circuit_on_run='no'))
    def open_circuit_on_run_no(self):
        message = "Is there a starting problem?"
        self.questions.append(message)
        self.expected_facts[message] = 'starting_problem'

    @Rule(CarDiagnosis(starting_problem='yes'))
    def starting_problem_yes(self):
        self.declare(CarDiagnosis(start_problem='yes'))

    @Rule(CarDiagnosis(starting_problem='no'))
    def starting_problem_no(self):
        message = "Is there an accessory failure?"
        self.questions.append(message)
        self.expected_facts[message] = 'accessory_failure'

    @Rule(CarDiagnosis(accessory_failure='yes'))
    def accessory_failure_yes(self):
        message = "Do all accessories fail?"
        self.questions.append(message)
        self.expected_facts[message] = 'all_accessories_fail'

    @Rule(CarDiagnosis(all_accessories_fail='yes'))
    def all_accessories_fail_yes(self):
        self.questions.append("Diagnostic: Accessory fuse first. Check accessory circuit for open.")

    @Rule(CarDiagnosis(all_accessories_fail='no'))
    def all_accessories_fail_no(self):
        self.questions.append("Diagnostic: Check power at accessory terminals. Check accessory ground mounting. Remove and test.")

    @Rule(CarDiagnosis(accessory_failure='no'))
    def accessory_failure_no(self):
        message = "Is the battery running down?"
        self.questions.append(message)
        self.expected_facts[message] = 'battery_running_down'

    @Rule(CarDiagnosis(battery_running_down='no'))
    def battery_running_down_no(self):
        message = "Is there a single lamp failure?"
        self.questions.append(message)
        self.expected_facts[message] = 'single_lamp_failure'

    @Rule(CarDiagnosis(single_lamp_failure='yes'))
    def single_lamp_failure_yes(self):
        self.questions.append("Diagnostic: Replace lamp, check ground, wire direct.")

    @Rule(CarDiagnosis(single_lamp_failure='no'))
    def single_lamp_failure_no(self):
        message = "Is there a blinker failure?"
        self.questions.append(message)
        self.expected_facts[message] = 'blinker_failure'

    @Rule(CarDiagnosis(blinker_failure='yes'))
    def blinker_failure_yes(self):
        self.questions.append("Diagnostic: Test with emergency flasher, swap blinker relay, bulb, switch failure.")

    @Rule(CarDiagnosis(blinker_failure='no'))
    def blinker_failure_no(self):
        self.questions.append("Diagnostic: Check fuse, failure in switch or wiring for multiple lamp failure, ie, headlights, emergency flashers, brake lights.")

    @Rule(CarDiagnosis(battery_running_down='yes'))
    def battery_running_down_yes(self):
        message = "Was the Alternator tested OK?"
        self.questions.append(message)
        self.expected_facts[message] = 'alternator_tested_ok'

    @Rule(CarDiagnosis(alternator_tested_ok='yes'))
    def alternator_tested_ok_yes(self):
        message = "Was the battery test OK?"
        self.questions.append(message)
        self.expected_facts[message] = 'battery_test_ok'

    @Rule(CarDiagnosis(battery_test_ok='yes'))
    def battery_test_ok_yes(self):
        self.questions.append("Diagnostic: Check hidden light drain, high computer draw, alarm system, etc...")

    @Rule(CarDiagnosis(battery_test_ok='no'))
    def battery_test_ok_no(self):
        self.questions.append("Diagnostic: Test specific gravity, levels. If inconclusive respan, replace.")

    @Rule(CarDiagnosis(alternator_tested_ok='no'))
    def alternator_tested_ok_no(self):
        message = "Is the voltage regulator good?"
        self.questions.append(message)
        self.expected_facts[message] = 'voltage_regulator_good'

    @Rule(CarDiagnosis(voltage_regulator_good='yes'))
    def voltage_regulator_good_yes(self):
        self.questions.append("Diagnostic: Check belt, grounds, all alternator connections, voltages.")

    @Rule(CarDiagnosis(voltage_regulator_good='no'))
    def voltage_regulator_good_no(self):
        self.questions.append("Diagnostic: Check voltage regulator ground, replace, otherwise control.")    