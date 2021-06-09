class College:
    no_of_branches=8
    var=8

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
        print(f'this is a good {string}')


class Player:
    no_of_games = 4 
    var=9

    def __init__(self,name,game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f'The name is {self.name}.\nThe game is {self.game}\n'



class CoolProgrammer(College,Player):           #1st class me constructor dhundhe ga then 2nd then 3rd .....
    languages='cpp'
    var=10

    def printlanguage(self):
        return(self.languages)

barinder=College('Barinder',20103010,"CSE")
mehakpreet=College('Mehakpreet',20105010,'ECE')
    
shubham = Player('Shubham',['cricket'])

karan=CoolProgrammer('Karan',20103059,'CSE')

print(karan.printdetails())
print(karan.printlanguage())

print(karan.var)

karan.printgood('valorant')
