#STUDENTS MARKS ANALYZER

"""
in this program,
I am gonna make a program where,
name and marks of the student will be entered and
it will analyze the marks and tell whether the student passed or failed.
"""

name = input("Name: ")
#marks out of 100

subject1 = int(input("Physics:"))
subject2 = int(input("Chemistry:"))
subject3 = int(input("Mathematics:"))
subject4 = int(input("English:"))
subject5 = int(input("Physical Education:"))

#now storing all subject marks in a list named marks.

marks = []
marks.append(subject1)
marks.append(subject2)
marks.append(subject3)
marks.append(subject4)
marks.append(subject5)

total_marks = (subject1 + subject2 + subject3 + subject4 + subject5)
print("total_marks:" , total_marks)
Percentage = (total_marks/500)*100
print("Percentage:", Percentage)

#highest marks and lowest marks will also be shown by using max() and min()


print("Highest Marks:" , max(marks))
print("Lowest Marks:" , min(marks))


"""
now in this program there will also be grade system,
it will  assign grade according to the marks scored in all the subjects,
through if-elif-else conditional
"""

if(total_marks >= 450):
    print("Grade:A")
    print("PASS")
elif(total_marks >= 400 and total_marks < 450 ):
    print("Grade:B")
    print("PASS")
elif(total_marks >= 350 and total_marks < 400 ):
    print("Grade:C")
    print("PASS")
elif(total_marks >= 300 and total_marks < 350):
    print("Grade:D")
    print("PASS")
elif(total_marks >= 250 and total_marks < 300):
    print("Grade:F")
    print("FAIL") 
else:
    print("FAIL")                   