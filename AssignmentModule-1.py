# Student Information

student_name = input("Enter Student Name: ")
student_id = input("Enter Student ID: ")
department = input("Enter Department: ")

print("\nStudent Information")
print("Name:", student_name)
print("ID:", student_id)
print("Department:", department)


# Subject Marks

subjects = ["Python", "Math", "English", "Physics", "ICT"]

marks = {}

for subject in subjects:
    mark = int(input(f"Enter marks for {subject}: "))
    marks[subject] = mark

print("\nSubject Marks:")
print(marks)

# Calculate Result
marks = {
    "Python": 90,
    "Math": 85,
    "English": 80,
    "Physics": 88,
    "ICT": 95
}

total_marks = sum(marks.values())
average_marks = total_marks / len(marks)
highest_mark = max(marks.values())
lowest_mark = min(marks.values())

print("\nResult")
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Highest Mark:", highest_mark)
print("Lowest Mark:", lowest_mark)

# Grade Calculation

average_marks = 75

if average_marks >= 80:
    grade = "A+"
elif average_marks >= 70:
    grade = "A"
elif average_marks >= 60:
    grade = "A-"
elif average_marks >= 50:
    grade = "B"
elif average_marks >= 40:
    grade = "C"
else:
    grade = "F"

print("\nGrade Calculation")
print("Average Marks:", average_marks)
print("Grade:", grade)

# Pass or Fail

python_marks = 75
math_marks = 65
english_marks = 38
science_marks = 80

if python_marks < 40 or math_marks < 40 or english_marks < 40 or science_marks < 40:
    status = "Failed"
else:
    status = "Passed"

print("Status:", status)


# Password Verification

correct_password = "python123"

password = input("Enter your password: ")

while password != correct_password:
    print("Incorrect Password!")
    password = input("Enter your password again: ")

print("Correct Password!")

# 7. String Operations
student_name = "Abu Jafar"

# Uppercase

print("Uppercase:", student_name.upper())

# Lowercase
print("Lowercase:", student_name.lower())

# Length
print("Length:", len(student_name))

# First three characters
print("First 3 characters:", student_name[:3])

# Last three characters
print("Last 3 characters:", student_name[-3:])

# 8. Set Example

sports = {"Football", "Cricket", "Badminton"}
clubs = {"Programming", "Cricket", "Photography"}

# Common items
common_items = sports.intersection(clubs)

# All unique items
all_unique_items = sports.union(clubs)

print("Common items:", common_items)
print("All unique items:", all_unique_items)


# 9. Tuple Example

weekdays = (
    "Saturday",
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
)

# First day
print("First day:", weekdays[0])

# Last day
print("Last day:", weekdays[-1])

# Total number of days
print("Total number of days:", len(weekdays))