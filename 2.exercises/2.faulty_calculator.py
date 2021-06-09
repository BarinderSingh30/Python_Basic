print('enter your first number')
num1=int(input())
print('enter your second number')
num2=int(input())



print('select your operation : ')
print("1 = addition \n","2 = subtraction \n","3 = multiplicatoin \n","4 = division \n")

op=int(input('enter your choice : '))

print('your answer is : ')
if (num1 == 45 and num2==3 and op==3) or (num2 == 45 and num1==3 and op==3):
    print(555)
elif (num1 == 56 and num2==9 and op==1) or (num1 == 9 and num2==56 and op==1):
    print(77)
elif (num1 == 56 and num2==6 and op==4) or (num1 == 6 and num2==56 and op==4):
    print(4)
elif op==1:
    print(num1+num2)
elif op==2:
    print(num1-num2)
elif op==3:
    print(num1*num2)
else:
    print(num1/num2)
    