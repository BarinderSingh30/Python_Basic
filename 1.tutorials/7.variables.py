var1="hello "
var2=7
var3=36.7
var4="barinder"
var5="32"
var6="54"
"""
int()
float()
string()
"""
print(type(var1))               # will show that it is a string.
print(type(var2))               # will show that it is a integer.
print(type(var3))               # will show that it is a floating value(decimal point).

print(var1+var4)
print(var2+var3)

print(var1+var5)                #it will concatenate(join) two text.
print(var5+var6)                # the output will be 3254 not 86.

print(int(var5)+int(var6))      # it will add these no. this is called type casting.

print(10*" hello world ")       # it will print hello world 10 times in the same line.
print(10*"hello world \n")      # it will print hello world 10 times in different lines.

print(10*(int(var5)+int(var6))) # now the output will be 10 times the addition of that numbers.

print(100*str(int(var5)+int(var6)))  # now the sum of that integers will be print 100 times.

print("enter your number")
num=input()                     # it will input the data in the form of string.

print("your number is=",num,"\n and also num+10= ", int(num)+10)

