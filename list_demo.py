str_names = ['Ankit','Chethan','Vishwas']
print(type(str_names))  # <class 'list'>

listx = [1,2,3,4,9,5,8,6,10,7]
#listx.sort()
#print(listx)

listx.append([11,15,17])
print(listx)

listx.insert(5,'Chethan')
print(listx)

listx.extend(['ABC','123'])
print(listx)
'''
Difference between append() and insert()
    append inserts just one elementlist at end of the list, 
    wheras insert func adds the element at given index.

Difference between append() and extend()
    append inserts just one element/list at end of the list, f you dd list, it ill be dded as listithin lit
    extend - always insert more than 1 element at once,[Basically we need to pass one more list]
    extend() -> Input is always an iterable object,it ill et da s list item

'''


listx=[1,2,3]
listy = listx.copy()
listz = listx

print("Values before change")
print(listx)
print(listy)
print(listz)

print("Values after change")
listz.append(14)
print(listx) #[12.345,13,18,14]
print(listy) # orig    
print(listz) #[12.345,13,18,14] 


