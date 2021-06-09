n=int(input('Enter the no. of rows :\n'))

b=int(input('Enter 1 for true or 0 for false\n'))


if b==1:
    b=True
else:
    b=False

if b:
    for i in range(1,n+1):
        print('*'*i)

else:
    for i in range(n,0,-1):
        print('*'*i)


