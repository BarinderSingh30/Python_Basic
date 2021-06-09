class Employee:
    no_of_leaves=8
    def printdetails(self):
        return f'Name is {self.name}\nSalary is {self.salary}\nROle is {self.role}'

Harry=Employee()
rohan=Employee()

Harry.name='Harry'
Harry.salary=500
Harry.role='Instructor'

rohan.name='Rohan'
rohan.salary=1000
rohan.role='student'


print(Harry.printdetails())         # it means harry is passed as argument in printdetails
print()



# ---------------------------------------CONSTRUCTOR---------------------------------------

class college:
    no_of_branches=8

    def __init__(self,aname,asid,abranch): #constructor to construct class object and assign their variables easily

        self.name=aname
        self.sid=asid
        self.branch=abranch
    
    def printdetails(self):
        return f'Name is {self.name}.\nSID is {self.sid}.\nBranch is {self.branch}'
        

barinder=college('Barinder',20103010,"CSE")
mehakpreet=college('Mehakpreet',20105010,'ECE')



print(barinder.printdetails())
print(mehakpreet.printdetails())
        