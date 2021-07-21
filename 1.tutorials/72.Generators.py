"""
Iterable - __iter__ or __getitem__()
Iterator - __next__()
Iteration-  
"""

def gen(n):
    for i in range(n):
        yield i



# for i in range(78):         #here range is a generetor
#     print(i)

g=gen(3456)         #g is used as generators

print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())


h= "harry"

# for c in h:
#     print(c)

# ier = h.__iter__()
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
