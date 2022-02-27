x = 2
x = 'Çhethan'
print(type(x))

'''
4 Ways to define String value
    1. ''
    2. " "
    3. ''' '''
    4. str() -> Inbuilt func
'''
str1 = 'Chethan'
print(str1)

# Using Double quote: When we want to print any string containing Single quote
str2 = "Chethan's firt String program"
print(str2)

# Using three single quote: When we want to print any string containing double quote
str3 = '''Hi, Welcome to "Chethan's Python" Course'''
print(str3)

name = 'Chethan'
print("Chethan name ends with n->" , name.endswith('n'))
print("Chethan name ends with N->" , name.endswith('N')) #Python is case sensitive

name = 'Chethan is good in py'
print(name.find('g'))

print(name.count('C'))

n = "This is the main"
print(n.title()) # This Is The Main... Capitaliza all the words in a sentence..Use case CNBC news update


fname = 'Chethan'
lname = 'çhethan'
print(fname+' '+lname)
print(fname.islower())
print(lname.islower())
print('vishu'.islower())

greeting = "Good Morning,this is Python Class"
print(greeting.index('Z'))

'''
Index() and find() both returns the starting position of substring or index of character.
But the difference is if there is no matching substring or char,
index() -> Returns error as : Substring not found
find() -> Returns -1
'''

