'''
List is a collection of elements that are ordered and "mutable" or "CHangeable". Allows duplicates.
Tuple is a collection of elements that are Odered and "Immutable" or "Unchangable". Allows duplicates.

list uses[] --- Square braces.
tuple uses() --- Normal braces
'''

tupleEg= ('Bangalore','Delhi','Pune')
print(tupleEg)

tupleEg1= ('Bangalore','Delhi','Pune','Noida',('Chethan','Vishu'))# Tuple within tuple
print("Demo of Tuple within Tuple  ->  "+ tupleEg1[4][1])

print()
print('''***"Packing" and "Unpacking with equal no of values"****''')
fruits = ('Grapes','Banana','Cherry') #Packing 3 values into one variable, that is fruit
(green,yellow,red) = fruits
print(green)
print(yellow)
print(red)


print('''***"Packing" and "Unpacking" without equal no****''')
fruits = ('Grapes','Banana','Cherry','Strawberry','rasperry',123,'Grapes') #Packing 5 values into one variable, that is fruit
(green,yellow,*red) = fruits #Unpacking values and assigning to left side variables

print(green)
print(yellow)
print(*red)# if u give 8 it will print all elements
print(red) #if u dont give *, it will print rest elemnts as a list
print("Tuple element count",  fruits.count('Grapes'))
print("Tuple index", fruits.index("Grapes")) #If there are duplicated, it prints first index
print("Tuple index", fruits.index("Strawberry"))

# How to print tuple using for loop
print("****************************")
print("Üsing for loop")
for x in fruits:
    print(x)

tuple1=(1,2,3)
tuple2=('a','b','c')
print(tuple2 + tuple1)


print(tuple2 * 2) # it print twice,as a tuple
print(tuple2 * 3) # it prints thrice

print("***************")
print("Modifying tuple")
tuple1= tuple1 *3  # Same thing as above, it prints thrice
print(tuple1)

for x in tuple1:
    print(x)






