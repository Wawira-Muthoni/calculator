#1.Add
#2. Subtract
#3. Multiply
#4. Divide
from select import EPOLLEXCLUSIVE


print("1. Addition")
print("2.Subtraction")
print("3. Multiplication")
print("4.Division")

choice =input("enter your choice : ")
num1 =float(input ("Enter Number 1: "))
num2 =input(float("Enter Number 2: "))

if choice =="1":
   print(num1, "+" ,num2, "=" ,(num1+num2))
elif choice =="2" : 
   print(num1,"-", num2,"=", (num1-num2)) 
elif choice == "3":
    print(num1,"*", num2,"=", (num1*num2)) 
elif choice =="4":
    if num2 == 0.0: 
        print ("Divide by 0 Error")
    else: 
     print(num1,"/", num2,"=",(num1/num2))

else:
    print("invalid choice")    