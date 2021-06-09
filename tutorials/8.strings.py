mystr="Barinder is a good boy"

print(len(mystr))                   # len() will print the length of the string.

print(mystr)                        #it will print the string/text.

print(mystr[7])         

"""
In python the string is a combinaitons of characters.The index of each string starts from 0 to characters-1
hence,in previous print statement it will print the 7th element of the string i,e. 8th character of that string=r.

"""
print(mystr[1:8])

"""
this concept is called string slicing.In which, some part of string will be printed.
SYNTAX 
print(variable[x:y])   - in this x,y are the indexes upto which we want to slice the string.
NOTE: Index x will be included and y will not, it means string will be sliced upto y-1 index.
"""


print(mystr[0:])            #it will print the whole string.

print(mystr[:8])            #it will automatically consider it as a zero.

print(mystr[:8887])         # it will print only upto the accessibility of string.

print(mystr[0:8:2])         

"""
now after the 2nd colon the no will show which index he has to go after printing first character,
for eg in barinder 2nd letter from b is r therefore it 
will print      brne      . this is called advanced slicing.

"""
print(mystr[::3])           # now the first place empty which means it will automatically consider full string.

print(mystr[::])            # it will print whole string.

"""
NOTE: it is important and somewhat advanced also.

Concept of negative indexes: -1 means last letter of the string, hence -2 means 2nd last digit
                                                                       -3 means 3rd last digit and so on.
"""

print(mystr[-4:-1])       #it means 4th last digit to last digit.
 
#   print(mystr[-1:2])  this will print nothing as there is nothing like minus to positive.

print(mystr[::-1])        # it will print the string in reverse order, as it is same as 1 just in reverse order.


print(mystr[::-2])        # same as 2 just in revrse order.


# some other functions
mystr2="barinderisagoodboy"

print(mystr.isalnum())    # return true if it is alphanumeric
print(mystr2.isalnum())

print(mystr.endswith(" boy")) # return true if it ends with the given syntax.
print(mystr2.endswith(" boy"))

print(mystr.count("is"))        # This function counts the total no. of occurrence of any character in the string.
print(mystr2.count("is"))

"""
string.capitalize(): This function capitalizes the first character of any string. It doesn’t take any argument.

string.upper(): It returns the copy of the string converted to the uppercase.

string.lower(): It returns the copy of the string converted to lower case.

string.find(): This function finds any given character or word in the entire string. It returns the index of first character from 
that word.//NOTE: in case if the occurence is more than 1 then first occurence one will be selected.

string.replace(“old_word”, “new_word”): This function replaces the old word or character with a new word or character from
 the entire string.

"""

print(mystr.find("o"))