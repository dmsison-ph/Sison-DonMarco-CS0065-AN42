facts = {
    "temperature_c": 32,       # Temperature
    "humidity_percent": 85,    # Moisture
    "is_raining": True,        # Moisture
    "windy": False,            # Weather condition
    "outdoor_planned": True,   # Activity
}

print("Current facts:")
for name, value in facts.items():
    print(f"- {name}: {value}")

def rule_rain(facts):
    if facts["is_raining"] and facts["outdoor_planned"]:
        return "Bring an umbrella"

def rule_heat(facts):
    if facts["temperature_c"] >= 30 and facts["outdoor_planned"]:
        return "Bring drinking water"
    
def rule_humidity(facts):
    if facts["humidity_percent"] >= 80 and facts["outdoor_planned"]:
        return "Take regular breaks"

rules = [rule_rain, rule_heat, rule_humidity]
actions = []

for rule in rules:
    action = rule(facts)
    if action is not None:
        actions.append(action)

print("\nRule-Based Reasoning Actions:")
if actions:
    for action in actions:
        print(f"- {action}")
else:
    print("- No action recommended")

case_base = [
    {
        "problem": {
            "temperature_c": 30,
            "humidity_percent": 80,
            "is_raining": True,
            "windy": False,
            "outdoor_planned": True,
        },
        "solution": "Bring an umbrella and water, and take breaks.",
    },
    {
        "problem": {
            "temperature_c": 24,
            "humidity_percent": 60,
            "is_raining": False,
            "windy": False,
            "outdoor_planned": True,
        },
        "solution": "Proceed with the outdoor activity.",
    },
    {
        "problem": {
            "temperature_c": 27,
            "humidity_percent": 75,
            "is_raining": True,
            "windy": True,
            "outdoor_planned": True,
        },
        "solution": "Consider postponing the outdoor activity.",
    },
]

print(f"\nPast cases available: {len(case_base)}")

def similarity(current, past):
    """Return a score from 0 to 1; higher means more similar."""
    temperature_score = max(
        0, 1 - abs(current["temperature_c"] - past["temperature_c"]) / 15
    )
    humidity_score = max(
        0, 1 - abs(current["humidity_percent"] - past["humidity_percent"]) / 40
    )

    rain_score = int(current["is_raining"] == past["is_raining"])
    wind_score = int(current["windy"] == past["windy"])
    activity_score = int(current["outdoor_planned"] == past["outdoor_planned"])

    return (
        temperature_score + humidity_score
        + rain_score + wind_score + activity_score
    ) / 5


print("\nCase-Based Reasoning Similarity Scores:")
for number, case in enumerate(case_base, start=1):
    score = similarity(facts, case["problem"])
    print(f"- Case {number}: {score:.3f}")

best_case = max(case_base, key=lambda case: similarity(facts, case["problem"]))
print("Most similar case:", case_base.index(best_case) + 1)

suggested_solution = best_case["solution"]
print("\nCBR suggested solution:", suggested_solution)

print("\nRevise the CBR solution:")
print("A. Keep the suggested solution")
print("B. Move the outdoor activity indoors because it is raining and humid")
print("C. Write my own solution")

while True:
    choice = input("Choose A, B, or C: ").strip().upper()

    if choice == "A":
        final_solution = suggested_solution
        break
    elif choice == "B":
        final_solution = (
            "Move the outdoor activity indoors because it is raining and humid."
        )
        break
    elif choice == "C":
        final_solution = input("Enter your solution: ").strip()
        if final_solution:
            break
        print("Please enter a solution.")
    else:
        print("Please choose A, B, or C.")

print("CBR final solution:", final_solution)

case_base.append({
    "problem": facts.copy(),
    "solution": final_solution,
})
print(f"Cases after retaining today's case: {len(case_base)}")
