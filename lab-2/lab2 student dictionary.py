# Student dictionary
student = {
    "Name": "Sarah",
    "ID": "DS-204",
    "Department": "Data Science",
    "CGPA": 3.45
}

# Print key and value using a for loop
for key in student:
    print(key, ":", student[key])

# Check academic standing
if student["CGPA"] >= 2.50:
    print("Status: Good Standing")
else:
    print("Status: Academic Warning")