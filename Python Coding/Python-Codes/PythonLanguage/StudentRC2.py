#This is a program to accept a student's name and scores in three subjects. Display the total, average
# and class secured based on the following criteria:
# 1st class: 60% and above
# 2nd class: 50% and above
# Pass class: Average score of 35 and above
# Fail: Average score below 35

student_name = input("Enter the student name: ")
student_subject1 = float(input("Enter the student subject1 marks: "))
student_subject2 = float(input("Enter the student subject2 marks: "))
student_subject3 = float(input("Enter the student subject3 marks: "))
total_marks = student_subject1 + student_subject2 + student_subject3
average = total_marks/3
if average >= 60:
    print("1st class")
elif average >= 50:
    print("2nd class")
elif average >= 35:
    print("Pass class")
else:    
    print("Fail")
