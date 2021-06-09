class College:
    type = 'engineering'            #public variable
    _location = 'Chandigarh'        #protected variable
    __country = "INDIA"             #private variable


class School(College):
    pass
class Garnde(School):
    pass

boy = School()
man = College()
child=Garnde()

print(man.type)
print(man._location)
print(man._College__country)


print(boy.type)
print(boy._location)

print(child._location)
#test test test test -------------------