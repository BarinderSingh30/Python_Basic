class Employee:
    no_of_leaves=8
    pass

Harry=Employee()
rohan=Employee()

Harry.name='Harry'
Harry.salary=500
Harry.role='Instructor'

rohan.name='Rohan'
rohan.salary=1000
rohan.role='student'


print(Harry.no_of_leaves)
print(rohan.no_of_leaves)
print(Employee.no_of_leaves)        #class member can be accesed by objects and class name, to change the value of member we use class name only.

print(rohan.__dict__)

Employee.no_of_leaves=9

rohan.no_of_leaves=10           #it will create rohan's variable.

print(rohan.__dict__)

print(rohan.no_of_leaves)
