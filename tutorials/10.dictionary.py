#dictionary is nothing but key values pair
d1={}
print(type(d1))

d2={"harry":"burger","rohan":"fish","binnnu":"roti","shubham":{"b":"roti","l":"fish","d":"chicken"}}
print(d2["harry"])              #it will print burger

print(d2["shubham"])            #it will print the dictionary

print(d2["shubham"]["b"])       # to acess even further

d2["ankit"]="maggi"
print(d2)             

del d2["ankit"]                 #to delete that entry    
print(d2)           

#d3=d2                           #it wont make anycopy of d2,if you edit d3 then d2 will also get edited.

d3=d2.copy()                    # it will make a copy of d2 and you can edit freely in d3.

del d3["harry"]

print(d2,"\n",d3)

d2.update({"leena":"chocolate"})    # it will update the value
print(d2)

print(d2.get("harry"))          # it will get the value corresponding to harry

print(d2.keys())                # it will show all the keys.

print(d2.items())               # it will show all the items .

