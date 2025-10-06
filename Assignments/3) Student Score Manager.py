
students_number_input = int(input("Enter number of students: "))

while students_number_input <= 0:
    print("Invalid input. Please enter a positive integer.")
    students_number_input = int(input("Enter number of students: "))

if students_number_input > 0:
    students_scores = []
    for i in range(students_number_input):

        name_input = input(f"Enter student {i + 1} name: ")

        # .strip() removes any spaces before and after the name.
        # .isalpha() then checks only the letters.
        while not name_input.strip().isalpha():
            print("Invalid input. Please enter a valid name (alphabetic characters only).")
            # Without the f, Python would print the curly braces literally instead of replacing them with variable values.
            name_input = input(f"Enter student {i + 1} name: ")

        score_input = float(input(f"Enter {name_input}'s score: "))
        while score_input < 0 or score_input > 100:
            print("Invalid input. Please enter a score between 0 and 100.")
            score_input = float(input(f"Enter {name_input}'s score: "))
        students_scores.append(score_input)

    average_score = sum(students_scores) / students_number_input
    highest_score = max(students_scores)
    lowest_score = min(students_scores)

    print(f"\nAverage Score: {average_score:.2f}")
    print(f"Highest Score: {highest_score:.2f}")
    print(f"Lowest Score: {lowest_score:.2f}")