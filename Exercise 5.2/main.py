# Don't Change code below line 
student_marks = [int(x) for x in input("Enter a list of students marks ").split()]
print(student_marks)
# Don't Change code above line
# Write your code below this line
highest_marks = 0
for marks in student_marks:
  if marks > highest_marks:
    highest_marks = marks

print(f"The highest marks in all subjects is : {highest_marks}")