def calculate_grade(marks):
    # Calculate average
    average = sum(marks) / len(marks)
    
    # Determine letter grade
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

# Call the function with 5 marks
my_marks = [82, 74, 90, 68, 77]
final_grade = calculate_grade(my_marks)

print("Final Grade:", final_grade)