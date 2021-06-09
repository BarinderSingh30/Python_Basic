class Dad:
    basketball = 1


class Son(Dad):
    dance=1
    def isdance(self):
        return f'Yes i can dance {self.dance} no of times'
    

class Grandson(Son):
    dance = 6

    def isdance(self):
        return f'oh yeah' \
             f'Yes i can dance {self.dance} no of times'

pam = Dad()

sam=Son()

dam=Grandson()

print(pam.basketball)
print(sam.basketball)
print(dam.basketball)

print(sam.isdance())
print(dam.isdance())

    