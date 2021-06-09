l1 = ["Bhindi", "Aloo", "chopsticks", "chowmein"]

# i = 1
# for item in l1:
#     if i%2 is not 0:
#         print(f"Jarvis please buy {item}")
#     i += 1

for index, item in enumerate(l1):
    if index%2==0:
        print(f"Jarvis please buy {item}")

iterable =[1,2,3,4]
  
enumerate(iterable, start=0)

list_1=["code","with","harry"]
for index,val in enumerate(list_1):
    print(index,val)                        

""" output : 0 code
1 with
2 harry"""

list_2 = ["Python", "Programming", "Is", "Fun"]
#Counter value starts from 5
result = enumerate(list_2, 5)
print(list(result))

"""
output:
[(5, 'Python'), (6, 'Programming'), (7, 'Is'), (8, 'Fun')]
"""

