class college:
    no_of_branches=8

    def __init__(self,aname,asid,abranch): #constructor to construct class object and assign their variables easily

        self.name=aname
        self.sid=asid
        self.branch=abranch
    
    def printdetails(self):
        return f'Name is {self.name}.\nSID is {self.sid}.\nBranch is {self.branch}'

    
    @classmethod
    def change_branches(cls,newbranches):
        cls.no_of_branches=newbranches

    @classmethod
    def alternativ_constructor(cls,string):
        # param=string.split('-')
        # return cls(param[0],param[1],param[2])
        return cls(*string.split('-'))
        

barinder=college('Barinder',20103010,"CSE")

mehakpreet=college('Mehakpreet',20105010,'ECE')



print(barinder.printdetails(),'\n')
print(mehakpreet.printdetails(),'\n')



barinder.change_branches(9)         #by using class method we can change the value of class members
print(barinder.no_of_branches)



harsh = college.alternativ_constructor('Harshdeep-20103059-CSE')            #hence new instance is created using class methods


print(harsh.printdetails())