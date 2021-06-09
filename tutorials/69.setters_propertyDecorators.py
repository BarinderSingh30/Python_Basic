#setters and property decorators

class Employee:
    def __init__(self,fname,lname) -> None:

        self.fname=fname
        self.lname=lname
        # self.email=f'{fname}.{lname}@gmail.com'

    def explain(self):
        return f'First name is {self.fname} and last name is {self.lname}'

    @property

    def email(self):
        if self.fname==None or self.lname ==None:
            return 'email is not set'
        return f'{self.fname}.{self.lname}@gmail.com'

    @email.setter
    def email(self,string):
        print('Setting now...')
        names = string.split('@')[0]
        self.fname = names.split('.')[0]
        self.lname = names.split('.')[1]

    @email.deleter

    def email(self):
        self.fname=None
        self.lname=None
    
barinder=Employee('Barinder','Singh')
harsh=Employee('Harshdeep','Singh')

print(barinder.explain())

print(barinder.email)

barinder.fname='Binnu'

print(barinder.email)           #first name is updated but email is still there?....so to resolve this we will use property decorator to hide the use of  funtion (encapsulation)

barinder.email = 'barinder.singh@gmail.com'

print(barinder.email , barinder.fname,barinder.lname)

del barinder.email

print(barinder.email)