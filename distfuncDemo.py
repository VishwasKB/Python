x={'one':[1,2,3]} #it works
print(x)

seteg=[1,2,3]
fz=frozenset(seteg)
x={fz:'one'} #it works,only immutable object.Hence use list set as frozenset. since key is an immuatble object
print(x)
#keys are imutable object (means it can be either a string,numbers,tuple,frozenset), cannot be duplicated,

y={}# empty dict
stringeg='ankit'
listx=['A','B','C']
y=y.fromkeys(listx,89)#it takes all the iterables and converts all individual elements
                        #into keys. If u dont give 89, default is none for all values
print(y)
print(type(y))