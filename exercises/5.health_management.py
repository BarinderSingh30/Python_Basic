


def getdate():
    import datetime
    return datetime.datetime.now()

while True:

    print('What do you want to do :\n1. Enter new client\'s details.\n2. Update existing client\'s details.\n3. Read the details.\n4.exit')
    inp1=int(input())



    if inp1==1:
        client_name=input('What is the client\'s name?\n')

        inp2=int(input('What do you want to do?\n1. Enter a diet\n2. Enter a excercise\n'))

        if inp2==1:
            while True:
                f=open(f'{client_name}_Diet.txt','a')
                diet=input('What is your diet? : \n')

                t=getdate()

                f.write(f'[{t}] : {diet}\n')
                
                f.close()

                flag=(input('Y : if you want to add more diet\nN : if you want to exit\n'))



                if flag=='n' or flag=='N':
                    break
        else:
            while True:
                f=open(f'{client_name}_Excercise.txt','a')

                exc=input('What is your Excercise? : \n')

                t=getdate()

                f.write(f'[{t}] : {exc}\n')
                
                f.close()

                flag=(input('Y : if you want to add more excercise\nN : if you want to exit\n'))

                if flag=='n' or flag=='N':
                    break

    elif inp1==2:
        client_name=input('What is the client\'s name?\n')

        inp2=int(input('What do you want to do?\n1. Enter a diet\n2. Enter a excercise\n'))

        if inp2==1:
            while True:
                f=open(f'{client_name}_Diet.txt','a')
                diet=input('What is your diet? : \n')

                t=getdate()

                f.write(f'[{t}] : {diet}\n')
                
                f.close()

                flag=(input('Y : if you want to add more diet\nN : if you want to exit\n'))



                if flag=='n' or flag=='N':
                    break



                
        else:
            while True:
                f=open(f'{client_name}_Excercise.txt','a')

                exc=input('What is your Excercise? : \n')

                t=getdate()

                f.write(f'[{t}] : {exc}\n')
                
                f.close()

                flag=(input('Y : if you want to add more excercise\nN : if you want to exit\n'))

                if flag=='n' or flag=='N':
                    break
    elif inp1==3:
        client_name=input('what is the name of the client?\n')
        inp3 = int(input('what do you want to read\n1. Diet\n2. excercise\n'))
        

        if inp3==1:
            f=open(f'{client_name}_Diet.txt','r')

            print(f.read())
            f.close()
        else:
            f=open(f'{client_name}_Excercise.txt','r')

            print(f.read())
            f.close()

    

    else:
        break



