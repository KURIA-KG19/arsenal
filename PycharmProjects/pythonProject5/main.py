#length = len(name)
#print(length)
#a=input("a:")
#b=input("b:")
#c=a
#a=b
#b=c
#print(a)
#print(b)
height = float(input("Enter height in metres"))
weight = float(input("Enter weight in kilograms"))
bmi = round(weight/height ** 2)
if bmi < 18.5:
    print(f"your bmi is {bmi} you are underweight")
elif bmi  < 25:
    print(f"your bmi is {bmi} you are normal weight")
elif bmi < 30:
    print(f"your bmi is {bmi} you are overweight")
elif bmi < 35:
    print(f"your bmi is {bmi} you are obese")
else:
    print(f"your bmi is {bmi}you are clinically obese")
#age=input("enter ypour curremt age")
#age_int = int(age)
#days = (90-age_int) * 365
#weeks = days/7
#weeks_float = int(weeks)
#months = (90 - age_int) * 12
#print(f"your have {days} days "+f"{weeks_float} weeks " + f" {months} months left")
#print("WELCOME TO THE TIP CALCULATOR")
#bill =float(input("What is the total bill"))
#tip = int(input("What is your tip percentage"))
#people = int(input("How many people will split the bill"))
#individual_bill =(bill * tip/100)/people
#final_bill = round(individual_bill, 2)
#print(f"Your individual bill is {final_bill} ")
#num = int(input("Please enter a number:"))
#if num%2==0 :
 #   print("EVEN NUMBER")
#else:
 #   print("odd number")
