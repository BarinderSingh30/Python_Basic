# ls = []
# for i in range(100):
#     if i%3==0:
#         ls.append(i)





# list comprehension
# ls =[i for i in range(100) if i%3==0]
# print(ls)







#dict comprehension : {0:'item0',1:'item1'}

# dict1 = {  i:f'item{i}' for i in range(1000) if i%10==0 }
# dict1 = {  i:f'Item{i}' for i in range(5)}
# dict1 = {value:key for key,value in dict1.items()}
# print(dict1)


#set comprehension

# dress ={i for i in {'dress1','dress2','dress1'}}
# print(dress)



#generator comprehension

# evens = (i for i in range(100) if i%2==0)
# print(type(evens))
# print(evens)

# for item in evens:
#     print(item)

# ls =[ [x,y] for x,y in enumerate([x for x in range(100) if x%2==0] )] 
# print(ls)