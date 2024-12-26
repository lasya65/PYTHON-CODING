#This is a program to accept student details and display the report card of the student.
student_name= input("Enter the student name: ")
student_rollno= input("Enter the student rollno: ")
student_class= input("Enter the student class: ")
student_section= input("Enter the student section: ")
student_subject1= int(input("Enter the student subject1 marks: "))
student_subject2= int(input("Enter the student subject2 marks: "))
student_subject3= int(input("Enter the student subject3 marks: "))
student_subject4= int(input("Enter the student subject4 marks: "))
student_subject5= int(input("Enter the student subject5 marks: "))
total_marks = student_subject1 + student_subject2 + student_subject3 + student_subject4 + student_subject5
percentage = (total_marks/500)*100
if percentage >= 90:
    print("Grade O")
elif percentage >= 80:
    print("Grade A")
elif percentage >= 70:
    print("Grade B")
elif percentage >= 60:
    print("Grade C")
elif percentage >= 50:
    print("Grade D")