grocery=["harpic","vim bar","deodrant","bhindi","lollypop",56] 
"""
this is called list and there is no need to define a list. it is a part ofpython syntax.
"""
print(grocery)              # it will rrint the whole list.
print(grocery[0])           # it will print the oth element of the list.
print(grocery[5])           

number=[2,5,3,11,8]


number.sort()   #it will convert it into accesending order.
print(number)

number.reverse()   #it will reverse the string(which is already sorted)
print(number)


"""
slicing is same as of string.

but it is advisible to not take extended parameter smaller than -1 as in default values it will wont effect but in custom
slicing it will effect.

and the output of the slicing of list is a list it self.
"""
number2=[1,2,3,4,5]
print(number2)

number2.append(7)        # it will add one more element at the end of the string.
print(number2)

num3=[]
num3.append(1)
num3.append(2)
num3.append(3)

print(num3)

num3.insert(2,69)    #it will insert the elemnt at the index which is specify there and shift every other by 1.
print(num3)          # syntax is list.insert(index,element)

grocery.insert(1,"pepsi")
print(grocery)

num3.remove(69)     #remove that parameter from the list
print(num3)     

grocery.pop()       #remove the specified element of the string.by default take the value -1 i.e., last
print(grocery)

"""
mutable: can change/
immutable:cannot change/

tuple is immutable, and list is mutable
you cannot change the value of tuple.
"""
num3[2]=666
print(num3)

tp=( 3,2,1)          # it is a tuple see the paranthesis
print(tp)

#tp[0]=34 it is incorrect

#tp=(1) is not a tuple you have to add atleast one comma.

# a=a+b, b=a-b , a=a-b , in python you can swap two numbers very easily.

# a,b=b,a

string='abcd'
l=list(string) #it converts string and make a list of it in l.
