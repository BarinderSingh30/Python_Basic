s = set()

# print(type(s))
# print(len(s))
#max , min 

s_from_list = set([1,2,3,4])

print(s_from_list)
print(type(s_from_list))

s.add(1) #to add element in set

s.add(1) #will only show 1 element as it only holds unique elements

s.add(2)

print(s)

s1 = s.union({1,2,3,4})

print(s,s1)

print(s.isdisjoint(s1))

s.remove(1)
print(s)