class College:
    no_of_branches=8

    def __init__(self,aname,asid,abranch): 

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
        return cls(*string.split('-'))

    @staticmethod
    def printgood(string):          
        print('this is a good')
        
class Programmer(College):

    def __init__(self, aname, asid, abranch,languages):
        self.name=aname
        self.sid=asid
        self.branch=abranch
        self.languages = languages
        
    
    def printprog(self):
        return f'Programmer\'s Name is {self.name}.\nHis SID is {self.sid}.\nHis branch is {self.branch}.\nThe languages are {self.languages}'


barinder=College('Barinder',20103010,"CSE")
mehakpreet=College('Mehakpreet',20105010,'ECE')


shubham=Programmer('Shubham',20103027,'CSE',['python'])
karan=Programmer("Karan",20103011,"CSE",['cpp'])

print(karan.printprog())

