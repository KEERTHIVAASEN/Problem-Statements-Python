print("STUDENT MARKSHEET ")
print("**********************")
regno = int(input("Enter your regno:"))
studentname = input("Enter your name:")
classname = input("Enter class name:")
mark1= int(input("Enter mark1:"))
mark2= int(input("Enter mark2:"))
mark3= int(input("Enter mark3:"))
mark4= int(input("Enter mark4:"))
mark5= int(input("Enter mark5:"))
total = mark1+mark2+mark3+mark4+mark5
percentage = total/5
if mark1 and mark2 and mark3 and mark4 and mark5 >= 40:
  if percentage >= 80:
      grade='A'
  elif percentage >=70:
      grade ='B'
  elif percentage >=60:
      grade = 'C'
  elif percentage >=40:
      grade = 'D'
  else:
      grade = 'F'
else:
   grade='F'
print("Register Number=",regno)
print("Student Name=",studentname)
print("Class=",classname)
print("Mark1=",mark1)
print("Mark2=",mark2)
print("Mark3=",mark3)
print("Mark4=",mark4)
print("Mark5=",mark5)
print("Total=",total)
print("Percentage=",percentage)
print("Grade=",grade)