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
        

barinder=college('Barinder',20103010,"CSE")

mehakpreet=college('Mehakpreet',20105010,'ECE')



print(barinder.printdetails(),'\n')
print(mehakpreet.printdetails())



college.change_branches(9)
print(college.no_of_branches)