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

    @staticmethod
    def printgood(string):          #staticmethod : will use only one argument i.e., string in this case, you can access it with class name and instance name both.
        print('this is a good')
        

barinder=college('Barinder',20103010,"CSE")

mehakpreet=college('Mehakpreet',20105010,'ECE')

harsh = college.alternativ_constructor('Harshdeep-20103059-CSE')            #hence new instance is created using class methods


harsh.printgood('machine')