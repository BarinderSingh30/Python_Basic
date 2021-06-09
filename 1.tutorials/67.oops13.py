#operator overloading and dunding method


class A:
    def __init__(self,name,salary,role) -> None:
        self.name=name
        self.salary=salary
        self.role=role

    def __add__(self,other):                #dunder method , help in operator overloading
        return self.salary + other.salary


    def __repr__(self) -> str:
        return f'His name is {self.name}.\nHis salary is {self.salary}.\nHis role is {self.role}.\n'

    def __str__(self) -> str:
        return 'who is the boss? hmm'


emp1=A('Barinder',400,"programmer")
emp2=A('harsh',1000,'coder')


print(emp1 + emp2)
print(emp1)
print(repr(emp1))