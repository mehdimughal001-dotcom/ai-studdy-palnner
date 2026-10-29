"""
AI Study Planner
A beginner-friendly study planner built with basic Python.
No AI API, database, GUI, or external packages are required.
"""

def get_positive_number(prompt, minimum, maximum=None):
    """Ask for a whole number within the allowed range."""
    while True:
        try:
            value = int(input(prompt))
            if value < minimum:
                print(f"Please enter a number of at least {minimum}.")
            elif maximum is not None and value > maximum:
                print(f"Please enter a number no greater than {maximum}.")
            else:
                return value
        except ValueError:
            print("Please enter a valid whole number.")


def create_study_plan(name, goal, days_per_week, hours_per_day):
    """Create a simple plan based on the student's goal and availability."""
    total_hours = days_per_week * hours_per_day

    day_names = [
        "Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"
    ]

    goal_lower = goal.lower()
    if "python" in goal_lower or "program" in goal_lower or "coding" in goal_lower:
        activities = [
            "Learn a new concept and write short notes",
            "Practice with small coding exercises",
            "Review examples and rewrite them yourself",
            "Build a tiny project using what you learned",
            "Fix errors and practice problem-solving",
            "Review the week's topics and improve your project",
            "Take a short quiz and note what to learn next"
        ]
    elif "math" in goal_lower or "mathematics" in goal_lower:
        activities = [
            "Study one core concept and write notes",
            "Solve practice questions",
            "Review worked examples",
            "Practice questions without looking at solutions",
            "Focus on difficult questions",
            "Review mistakes and retry questions",
            "Take a short self-test"
        ]
    elif "language" in goal_lower or "english" in goal_lower:
        activities = [
            "Learn new vocabulary and review grammar",
            "Practice reading and summarize a short text",
            "Listen to a short lesson or audio",
            "Write a short paragraph",
            "Practice speaking or pronunciation",
            "Review vocabulary and correct mistakes",
            "Read or listen to something enjoyable in the language"
        ]
    else:
        activities = [
            "Learn a new topic and take notes",
            "Practice the topic with examples",
            "Review your notes and explain the topic in your own words",
            "Complete a small exercise or task",
            "Focus on a challenging part of the subject",
            "Review the week's learning and practice",
            "Take a short self-test and plan what to learn next"
        ]

    plan_lines = [
        "MY PERSONALIZED STUDY PLAN",
        "=" * 30,
        f"Student name: {name}",
        f"Learning goal: {goal}",
        f"Study days per week: {days_per_week}",
        f"Study hours per day: {hours_per_day}",
        f"Total study hours per week: {total_hours}",
        "",
        "YOUR WEEKLY SCHEDULE",
        "-" * 30,
    ]

    for index in range(days_per_week):
        day = day_names[index]
        activity = activities[index]
        plan_lines.append(f"{day} ({hours_per_day} hour(s)): {activity}")

    plan_lines.extend([
        "",
        "STUDY TIPS",
        "-" * 30,
        "1. Put your phone away during focused study time.",
        "2. Take a short break between study sessions.",
        "3. Practice what you learn instead of only reading.",
        "4. Review your progress at the end of each week.",
        "5. Adjust the plan when your schedule or goal changes.",
        "",
        "Keep going—small, regular steps lead to progress!"
    ])

    return "\n".join(plan_lines)


def main():
    print("=" * 35)
    print("       AI STUDY PLANNER")
    print("=" * 35)

    name = input("What is your name? ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("What is your name? ").strip()

    goal = input("What is your AI or learning goal? ").strip()
    while not goal:
        print("Please enter a learning goal.")
        goal = input("What is your AI or learning goal? ").strip()

    days = get_positive_number("How many days per week can you study (1-7)? ", 1, 7)
    hours = get_positive_number("How many hours can you study each study day? ", 1)

    plan = create_study_plan(name, goal, days, hours)

    print("\n" + plan)

    try:
        with open("study_plan.txt", "w", encoding="utf-8") as file:
            file.write(plan)
        print("\nYour study plan has been saved to study_plan.txt.")
    except OSError as error:
        print(f"Could not save the study plan: {error}")


if __name__ == "__main__":
    main()
