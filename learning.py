import os 
import datetime
print(datetime.datetime.now() ," this is the program to learn ")
print (" hello to my tiny programing world ")
student= input("enter the student name :")
student_id=  int(input("enter the ID number of your card :"))
if student == "hari" and student_id !="007":
    print ("good to go ")
elif student =="janaa" and student_id == "007":
    print("not a student of the department") 
    print("not allowed")
    
else :
    print("your good to go ")
