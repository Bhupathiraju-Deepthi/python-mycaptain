# working of upper() function
text = 'my name is Deepthi'

# upper() function to convert
# string to upper case
print("\nConverted String:")
print(text.upper())

# lower() function to convert
# string to lower case
print("\nConverted String:")
print(text.lower())

# converts the first character to
# upper case and rest to lower case
print("\nConverted String:")
print(text.title())

# original string never changes
print("\nOriginal String")
print(text)
# Python program to demonstrate the
# use of capitalize() function

# capitalize() first letter of string
# and make other letters lowercase
print(text.capitalize())

# Python program to convert string in lower case

# print lowercase string
print("lowercase string: ",text.casefold())

# Python program to illustrate
# string center() in python

new_string = text.center(12)
print ("After padding String is: ", new_string)
# count() method without optional parameters

# string in which occurrence will be checked

# counts the number of times substring occurs in
# the given string and returns an integer
print(text.count("Deepthi"))
# encode()

# printing the encoded string
print ("The encoded string in utf8 format is : ",)
print (text.encode('utf8', 'ignore'))

# .endswith() function


# returns False
result = text.endswith('my')
print (result)

# returns True
result = text.endswith('Deepthi')
print (result)

# returns True
result = text.endswith('my name is Deepthi')
print (result)

# working of expandtabs()

# initializing string
str = "i\tlove\t ftuo"

# using expandtabs to insert spacing
print("Modified string using default spacing: ", end ="")
print(str.expandtabs())

print("\r")

# using expandtabs to insert spacing
print("Modified string using less spacing: ", end ="")
print(str.expandtabs(2))

print("\r")

# using expandtabs to insert spacing
print("Modified string using more spacing: ", end ="")
print(str.expandtabs(12))

print("\r")

# returns first occurrence of Substring
result = text.find('Deepthi')
print ("Substring 'Deepthi' found at index:", result )

result = text.find('for')
print ("Substring 'for ' found at index:", result )

# How to use find()
if (text.find('deepu') != -1):
	print ("Contains given substring ")
else:
	print ("Doesn't contains given substring")
	
# the str.format() method

# using format option in a simple string
print("{}, hello."
	.format("deepthi"))

# using format option for a
# value stored in a variable
str = "This is {}"
print(str.format("Python"))

# formatting a string using a numeric constant
print("Hello, I am {} years old !".format(20))

# input stored in variable a.
a = {'x':'John', 'y':'Wick'}

# Use of format_map() function
print("{x}'s last name is {y}".format_map(a))
# index()

# initializing target string
ch = "hello maddy"

# initializing argument string
ch1 = "maddy"

# using index() to find position of "maddy"
pos = ch.index(ch1,2)

print ("The first position of maddy after 2nd index : ",end="")
print (pos)

# isalnum() method

# here a,b and c are characters and 1,2 and 3
# are numbers
string = "abc123"
print(string.isalnum())

string = "abc 123"
print(string.isalnum())

#  isalpha()

# checking for alphabets
string = 'deepthi'
print(string.isalpha())

string = 'deepthi34'
print(string.isalpha())

# checking if space is an alphabet
string = 'Bhupathiraju Deepthi'
print( string.isalpha())

# isdecimal()

s = "12345"
print(s.isdecimal())

# contains alphabets
s = "deepthi34"
print(s.isdecimal())

# contains numbers and spaces
s = "12 34"
print(s.isdecimal())

# isdigit()

# checking for digit
string = '15460'
print(string.isdigit())

string = 'deepthi60'
print(string.isdigit())

# the working of isidentifier()

# String with spaces
string = "my name is deepthi"
print(string.isidentifier())

# A Perfect identifier
string = "mynameisdeepthi"
print(string.isidentifier())

# Empty string
string = ""
print(string.isidentifier())

# Alphanumerical string
string = "my0name0is0deepthi"
print(string.isidentifier())

# Beginning with an integer
string = "34my0name0is0deethi"
print(string.isidentifier())


# Python code for implementation of isnumeric()
	
# checking for numeric characters
string = '123deepu456'
print(string.isnumeric())

string = '123456'
print( string.isnumeric())

# Python code for implementation of isprintable()

# checking for printable characters
string = 'My name is deepthi'
print(string.isprintable())

# checking if \n is a printable character
string = 'My name is \n deepthi'
print(string.isprintable())

# checking if space is a printable character
string = ''
print( string.isprintable())

# Python code for implementation of isspace()

# checking for whitespace characters
string = 'mynameisdeepthi'

print(string.isspace())

# checking if \n is a whitespace character
string = '\n \n \n'

print(string.isspace())

string = 'my\nname\nis\ndeepthi'
print( string.isspace())

# First character in each word is
# uppercase and remaining lowercases
s = 'My Name Is Deepthi'
print(s.istitle())

# First character in first
# word is lowercase
s = 'my Name Is Deepthi'
print(s.istitle())

# Third word has uppercase
# characters at middle
s = 'My Name is DEEpthi'
print(s.istitle())

s = '6041 Is My Number'
print(s.istitle())

# word has uppercase
# characters at middle
s = 'DEEPTHI'
print(s.istitle())
# working of isupper()


# use of join function to join list
# elements with a character.

list1 = ['1','2','3','4']

s = "-"

# joins elements of list1 by '-'
# and stores in sting s
s = s.join(list1)

# join use to join a list of
# strings to a separator s
print(s)

# lstrip() method using default parameter
	
# string which is to be stripped
string = " Deepthi"
	
# Removes spaces from left.
print(string.lstrip())


string = "deepthi is  good"

# 'is' separator is found
print(string.partition('is '))

# 'not' separator is not found
print(string.partition('bad '))

string = "deepthi is a good, isn't it"

# splits at first occurrence of 'is'
print(string.partition('is'))

# use of replace() method

string = "deepthi is deepthi deepthi deepthi"

# Prints the string by replacing all
# geeks by Geeks
print(string.replace("deepthi", "DEEPTHI"))

# Prints the string by replacing only
# 3 occurrence of Geeks
print(string.replace("deepthi", "DEepthi", 3))

# Python program to demonstrate working of rfind()
# in whole string
word = 'my name is deepthi is deepthi'

# Returns highest index of the substring
result = word.rfind('deepthi')
print ("Substring 'deepthi' found at index :", result )

result = word.rfind('is')
print ("Substring 'is' found at index :", result )

word = 'CatBatSatMatGate'

# Returns highest index of the substring
result = word.rfind('ate')
print("Substring 'ate' found at index :", result)
# Python code to demonstrate working of rindex()
text = 'deepthi is deepthi'

result = text.rindex('deepthi')
print("Substring 'deepthi':", result)

#  rpartition()

# String need to split
string1 = "deepthi@is@deepthi@is@for@deepthi"

string2 = "deepu is not eating but deepthi is eating"

# Here '@' is a separator
print(string1.rpartition('@'))

# Here 'is' is separator
print(string2.rpartition('is'))

# Python code to split a string
# using rsplit.

# Splits at space
word = 'geeks for geeks'
print(word.rsplit())


word = 'deepthi, for, deepthi'
print(word.rsplit('d', 1))

word = 'deepthi@for@deepthi'
print(word.rsplit('@', 1))

# rstrip() method using optional parameters

# string which is to be stripped
string = "deepsss"

# Removes given set of characters from
# right.
print(string.rstrip('s'))

# Python code to illustrate splitlines()
string = "Welcome everyone to\rthe world of deepthi\n"

# No parameters has been passed
print (string.splitlines( ))

# A specified number is passed
print (string.splitlines(0))

# True has been passed
print (string.splitlines(True))

# Python code shows the working of
# .startsswith() function

text = "deepthi likes chocolates"

# returns False
result = text.startswith('likes chocolate')
print (result)

# returns True
result = text.startswith('deepthi')
print (result)

# returns False
result = text.startswith('likes chocolate.')
print (result)

# returns True
result = text.startswith('deepthi likes chocolates')
print (result)

# strip() method

string = """   deepthi likes chocolates   """

# prints the string without stripping
print(string)

# prints the string by removing leading and trailing whitespaces
print(string.strip())

# prints the string by removing geeks
print(string.strip(' deepthi'))
# swapcase() method

string = "DeePThilikesCHOcolates"

# prints after swappong all cases
print(string.swapcase())

string = "striver"
print(string.swapcase())

# translations without
# maketrans()

# specifying the mapping
# using ASCII
table = { 119 : 103, 121 : 102, 117 : None }

# target string
trg = "weeksyourweeks"

# Printing original string
print ("The string before translating is : ", end ="")
print (trg)

# using translate() to make translations.
print ("The string after translating is : ", end ="")
print (trg.translate(table))
text = "deepthi likes chocolates"

print(text.zfill(117))

print(text.zfill(45))

# Given length is less than
# the length od original string
print(text.zfill(10))

txt = "hello world!"

x = txt.islower()

print(x)
txt = "THIS IS NOW!"

x = txt.isupper()

print(x)
txt = "banana"

x = txt.rjust(20)

print(x, "is my favorite fruit.")
txt = "Company123"

x = txt.isascii()

print(x)






