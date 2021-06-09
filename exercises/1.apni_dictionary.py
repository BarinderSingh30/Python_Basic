dicc = {'sullen':"bad tempered person / don't want to talk to anyone.",'worm': 'to move slowly','morose':'bad tempered / not saying much to other people  (mood)'
,'terrific':'extrememly nice , excellent' ,'terrible':'very unpleasent , very upset'}

z=input("Enter your word : ")

print('meaning of your word',end=" : ")
print(dicc.get(z))