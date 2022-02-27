# Set is collection of items, which are Ünordered, Unindexed. Allows duplicated, but it will remove duplicates while printing
'''
Set uses {}- curly braces.
There is nothing called emptyset.
seteg={} 
empty set is nothing but empty dict.
'''

setex={1,2,3,'chethan'}
print(setex) # it can print in any order, try executing multiple times
seteg={1,2,3,'ankit',1,2,2,1,2,1,2,'ankit'} # Set allows duplicates, but remove duplicates while printing, hence indexing is not applicable/

print(seteg)

print("Union of sets")
set1={1,2,3,4,5}
set2={6,7,8}
print(set1.union(set2))
print(set1|set2)

print("Intersection of sets")
set1={1,4,5,7}
set2={5,6}
print(set1.intersection(set2))
print(set1 & set2)


oldset = {1,2,3,4,5,6}
newset = oldset.add('Chethan')
print(newset)
print(oldset)

#oldset.add(['Chethan']) #TypeError: unhashable type: 'list' , We cannot add elemnts using list 
#print(oldset)
