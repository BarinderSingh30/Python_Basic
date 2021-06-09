n= 18
i=1
while i <=9:
    z=int(input())

    if z>18:
        print('your number is greater than the mystry number')
    elif z<18:
        print('your number is smaller than the mystry number')
    elif z==18:
        print("booooyah !")
        break
    i+=1
if i <=9:
    print('you got the answer')
else:
    print('GAME OVER ......better luck next time')




