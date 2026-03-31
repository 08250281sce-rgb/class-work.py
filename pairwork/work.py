name =(input ("enter name:"));
print(name)
module_1= float(input("enter mark1:"));
module_2= float(input("enter mark2:"));
module_3= float(input("enter mark3:"));
module_4= float(input("enter mark4:"));
total_mark= module_1 + module_2 + module_3 + module_4
average = total_mark/4
print ("The average of your marks is ""%.2f" % (average))
attendance = float (input("enter your total attendance:"));
if (attendance >70):
    print("you are eligible for the exam")
else: 
    print("you are not eligible for the exam")

if (average >90):
    print("eligible for the reward")
else:
    print("reward is not posiible this time,try next semester.")

if (average >40):
    print(" congargulation! you have passed the exam")
else:
    print(" Therfore you have failed")           

if (average >= 90 ):
    print("Grade A")
elif(average >= 80 ):
    print("Grade B")
elif (average >= 70):
    print("Grade C")
elif (average >= 60):
    print("Grade D")
elif (average >= 50):
    print("Grade E")  
