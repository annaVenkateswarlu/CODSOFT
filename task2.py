print("Welcome to Simple Calculator")
print("Enter a two numbers")
First_Number=int(input())
Secound_Number=int(input())
print("1.Addition\n2.Subtration\n3.Multiplication\n4.Division")
Choice=int(input())
if Choice==1:
    print("The Addition of "+str(First_Number)+" and "+str(Secound_Number)+" is - "+str(First_Number+Secound_Number))
elif Choice==2:
    print("The Subtration of "+str(First_Number)+" and "+str(Secound_Number)+" is - "+str(First_Number-Secound_Number))
elif Choice==3:
    print("The Multiplication of "+str(First_Number)+" and "+str(Secound_Number)+" is - "+str(First_Number*Secound_Number))
elif Choice==4:
    print("The Division of "+str(First_Number)+" and "+str(Secound_Number)+" is - "+str(First_Number/Secound_Number))
else:
    print("Enter a Vaild Number")