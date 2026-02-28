from TrekPhysics import Hiker, Atmosphere, Respiration, TrekVisualizer
import sys

def get_valid_number(prompt, data_type=float):
    while True:
        try:
            val = data_type(input(prompt))
            if val < 0:
                print("Error: Positive number required.")
                continue
            return val
        except ValueError:
            print("Error: Invalid input.")

print("\n" + "="*40)
print("     TREK PHYSICS: TRIP PLANNER     ")
print("="*40)

# Inputs
print("--- Step 1: Hiker Stats ---")
weight = get_valid_number("Enter body weight (kg): ")
pack = get_valid_number("Enter pack weight (kg): ")

print("\n--- Step 2: Trip Details ---")
speed = get_valid_number("Enter walking speed (m/s) [Avg 1.2]: ")
incline = get_valid_number("Enter slope gradient (%) [Avg 5-10]: ")
distance = get_valid_number("Enter trip distance (km): ")

print("\n--- Step 3: Environment ---")
altitude = get_valid_number("Enter target altitude (meters): ")

# Analysis
print(f"\n{'='*30}")
print("       SCIENTIFIC ANALYSIS       ")
print(f"{'='*30}")

try:
    # 1. Biomechanics
    user = Hiker(body_mass_kg=weight, pack_weight_kg=pack)
    calories_hr = user.get_calorie_burn(velocity_ms=speed, gradient_percent=incline)
    duration_hours = (distance * 1000) / (speed * 3600)
    total_trip_cal = calories_hr * duration_hours

    print(f"\n[1] METABOLICS")
    print(f"    Burn Rate: {calories_hr} kcal/hour")
    print(f"    Total Energy: {round(total_trip_cal, 0)} kcal")

    # 2. Physiology (Updated with Heart Rate)
    medic = Respiration()
    water_req = medic.calculate_hydration_need(calories_hr, altitude)
    risk = medic.assess_risk(altitude)
    blood = medic.estimate_blood_metrics(altitude)

    print(f"\n[2] INTERNAL BIOPHYSICS")
    print(f"    Est. SpO2 (Blood Oxygen): {blood['spo2']}%")
    print(f"    Heart Rate: {blood['cardio_status']}")
    print(f"    Hypoxia Risk: {risk}")
    print(f"    Hydration Plan: Drink {water_req} Liters/hour")

    # 3. Atmosphere
    air = Atmosphere(altitude_meters=altitude)
    print(f"\n[3] EXTERNAL ATMOSPHERE at {altitude}m")
    print(f"    Boiling Point: {air.boiling_point} °C")
    print(f"    Cooking Adjust: {air.cook_time_multiplier}x longer")

    # 4. Load Optimization
    print(f"\n[4] LOAD OPTIMIZATION")
    check_item = input("Do you want to calculate the cost of an extra item? (y/n): ").lower()
    if check_item == 'y':
        item_name = input("    Item name (e.g., Camera): ")
        item_weight = get_valid_number("    Item weight (kg): ")
        penalty = user.calculate_item_penalty(item_weight, distance, speed, incline)
        print(f"    >> Carrying '{item_name}' will cost you {penalty} EXTRA Calories.")

    # 5. Visualization
    show_graph = input("\nShow Visual Graph? (y/n): ").lower()
    if show_graph == 'y':
        print("Generating graph...")
        start_alt = get_valid_number("Enter Starting Altitude (for graph) (meters): ")
        trek_profile = [start_alt, start_alt + (altitude - start_alt)*0.3, altitude, altitude, start_alt]
        plotter = TrekVisualizer(trek_profile)
        plotter.plot_environmental_impact()
except Exception as e:
    print(f"\nAn error occurred: {e}")