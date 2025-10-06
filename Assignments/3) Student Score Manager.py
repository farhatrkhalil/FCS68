students_number_input = int(input("Enter number of students: "))

while students_number_input <= 0:
    print("Invalid input. Please enter a positive integer.")
    students_number_input = int(input("Enter number of students: "))

if students_number_input > 0:
    students_names = []
    students_scores = []
    Failed_students = []
    for i in range(students_number_input):

        name_input = input(f"Enter student {i + 1} name: ")

        # .strip() removes any spaces before and after the name.
        # .isalpha() then checks only the letters.
        while not name_input.strip().isalpha():
            print("Invalid input. Please enter a valid name (alphabetic characters only).")
            # Without the f, Python would print the curly braces literally instead of replacing them with variable values.
            name_input = input(f"Enter student {i + 1} name: ")
        students_names.append(name_input)

        score_input = float(input(f"Enter {name_input}'s score: "))
        while score_input < 0 or score_input > 100:
            print("Invalid input. Please enter a score between 0 and 100.")
            score_input = float(input(f"Enter {name_input}'s score: "))
        if score_input < 60:
            Failed_students.append(name_input)

        students_scores.append(score_input)

    average_score = sum(students_scores) / students_number_input
    highest_score = max(students_scores)
    top_index = students_scores.index(highest_score)
    highest_score_student_name = students_names[top_index]

    print("\nAll students and scores:")
    for i in range(students_number_input):
        print(f"{students_names[i]} - {students_scores[i]:.0f}")

    # 2f means “floating-point number with 0 or 1 or 2 digits after the decimal point.”
    print(f"\nAverage score: {average_score:.1f}")
    print(f"Top student: {highest_score_student_name} ({highest_score:.0f})")
    print(f"Failed students: {', '.join(Failed_students)}")

