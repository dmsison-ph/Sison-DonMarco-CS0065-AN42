# Case Study 3: Intelligent Tutoring System
new_problem = {
    "topic": "linear_equations",
    "error_type": "sign_error",
    "repeated_errors": 3,
    "needs_visual_example": True,
}


print("=======================================================")
print("\t    LEARNING FROM STUDENT MISTAKES")
print("\tA Case-Based Intelligent Tutoring System")
print("\t\tTA3 | Sison & Millan")
print("=======================================================")
print("New student problem:")
print(f"- Topic: {new_problem['topic']}")
print(f"- Error pattern: {new_problem['error_type']}")
print(f"- Times the error was repeated: {new_problem['repeated_errors']}")
print(f"- Needs a visual example: {new_problem['needs_visual_example']}")

case_base = [
    {
        "problem": {
            "topic": "linear_equations",
            "error_type": "sign_error",
            "repeated_errors": 1,
            "needs_visual_example": True,
        },
        "solution": {
            "feedback": "Check the sign when moving a term across the equals sign.",
            "exercise": "Solve 3x - 5 = 10, showing each step.",
        },
    },
    {
        "problem": {
            "topic": "linear_equations",
            "error_type": "distribution_error",
            "repeated_errors": 3,
            "needs_visual_example": True,
        },
        "solution": {
            "feedback": "Distribute the number to every term inside the parentheses.",
            "exercise": "Expand 2(x + 3), then solve 2(x + 3) = 14.",
        },
    },
    {
        "problem": {
            "topic": "fractions",
            "error_type": "sign_error",
            "repeated_errors": 3,
            "needs_visual_example": False,
        },
        "solution": {
            "feedback": "Track the sign of each number before combining fractions.",
            "exercise": "Calculate -1/2 + 3/4 and explain the sign of the answer.",
        },
    },
]

print(f"\nPast tutoring cases available: {len(case_base)}")

def similarity(new, past):
    """Score similarity out of 10 points."""
    score = 0

    if new["topic"] == past["topic"]:
        score += 3
    if new["error_type"] == past["error_type"]:
        score += 4
    if new["needs_visual_example"] == past["needs_visual_example"]:
        score += 1

    # Up to 2 points for a similar number of repeated errors.
    difference = abs(new["repeated_errors"] - past["repeated_errors"])
    score += 2 * max(0, 1 - difference / 4)

    return score


print("\nSimilarity to past cases:")
for number, case in enumerate(case_base, start=1):
    score = similarity(new_problem, case["problem"])
    print(f"- Case {number}: {score:.1f}/10")

best_number, best_case = max(
    enumerate(case_base, start=1),
    key=lambda item: similarity(new_problem, item[1]["problem"]),
)

print(f"\nRetrieved Case {best_number}:")
print("Problem:", best_case["problem"])
print("Past feedback:", best_case["solution"]["feedback"])
print("Past exercise:", best_case["solution"]["exercise"])

adapted_solution = best_case["solution"].copy()

if new_problem["repeated_errors"] >= 3:
    adapted_solution["feedback"] += (
        " Since this error happened repeatedly, check the sign after "
        "each algebra step before continuing."
    )
    adapted_solution["exercise"] += (
        " Then solve 4x - 7 = 9 using the same steps."
    )

if new_problem["needs_visual_example"]:
    adapted_solution["visual_example"] = (
        "3x - 5 = 10 → add 5 to both sides → "
        "3x = 15 → divide both sides by 3 → x = 5."
    )

print("\nAdapted tutoring solution:")
print("Feedback:", adapted_solution["feedback"])
print("Practice:", adapted_solution["exercise"])
if "visual_example" in adapted_solution:
    print("Worked example:", adapted_solution["visual_example"])

new_case = {
    "problem": new_problem.copy(),
    "solution": adapted_solution.copy(),
}
case_base.append(new_case)

print("\nNew case saved to the case base for this run.")
print(f"Updated case base: {len(case_base)} cases")
for number, case in enumerate(case_base, start=1):
    print(
        f"- Case {number}: "
        f"{case['problem']['topic']}, "
        f"{case['problem']['error_type']}, "
        f"{case['problem']['repeated_errors']} repeated error(s)"
    )
