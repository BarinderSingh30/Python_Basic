#----------------------Library management----------------------------------------------

# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input


#can be used at the backend by changing some things, and also can add alot more feature its just a prototype
#---------------------------------------------------------------------------------------------------------------------
import time

class Library:
    global listofbooks
    lendbook_data={}

    #constructor
    def __init__(self,list_of_books,library_name) -> None:
        
        self.listofbooks =list_of_books
        self.libraryname = library_name


    # to dispay the books
    def display(self):
        print('The available books are :')
        for i in range(len(listofbooks)):
            print(listofbooks[i])
        time.sleep(3)

    # to add the book to the library bank
    def add_book(self,bookname):
        listofbooks.append(bookname)

    #to lend a book from the library
    def lend_book(self,bookname,username):
        if self.lendbook_data.get(bookname) ==None:
            print('Hope you will get something out of the book')
            self.lendbook_data[bookname] = username
        else:
            print('sorry we don\'t have the book right now')
            time.sleep(3)


    #to save the returning book from the library , edit: fine system can be applied if required
    def returning_thebook(self,bookname,username):
        if self.lendbook_data.get(bookname)==None:
            print('sorry, but this book is not belong to the library')
            time.sleep(3)
        else:
            print('thanks for returning the book')
            del self.lendbook_data[bookname]
        



#By default :

listofbooks = ['kaizen','juglebook','kux to log khenge','the man who knew infinity']
libraryname = 'Monty\'s python flying library'

obj1=Library(listofbooks,libraryname)




if __name__ == '__main__':

    print(f'Welcome to the {obj1.libraryname}.\nWhat is your name?')

    username=input()

    exit = False
    while not exit :

        

        print('\nWhat doy you want to do?\n1.Display the books.\n2.Donate a books\n3.Lend a book.\n4.return a book.\n5.Exit\n')

        inp1=int(input('Input a number to select your choice -:\n'))


        if inp1==1:
            obj1.display()

        elif inp1==2:
            bookname=input('\nEnter the name of the book and thanks for your humble gesture : \n')
            obj1.add_book(bookname)

        elif inp1==3:
            bookname=input('\nEnter the name of the book you want : \n')
            obj1.lend_book(bookname,username)
        
        elif inp1==4:
            bookname=input('\nEnter the name of the book and thanks for the returning : \n')
            obj1.returning_thebook(bookname,username)

        elif inp1==5:
            exit=True
            print('Thanks for coming to the library , have a nice day')













