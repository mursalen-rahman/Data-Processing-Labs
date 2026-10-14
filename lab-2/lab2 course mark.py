# List containing marks of 5 courses
marks = [75, 45, 88, 52, 60]

# Calculations
total_marks = sum(marks)
average_mark = total_marks / len(marks)
highest_mark = max(marks)
lowest_mark = min(marks)

# Count passed courses (pass mark = 50)
passed_courses = 0
for mark in marks:
    if mark >= 50:
        passed_courses = passed_courses + 1

# Display results
print("Total Marks:", total_marks)
print("Average Mark:", average_mark)
print("Highest Mark:", highest_mark)
print("Lowest Mark:", lowest_mark)
print("Courses Passed:", passed_courses)