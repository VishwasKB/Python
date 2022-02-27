# 2 dim data that means we are talking about two variables
# introduces key:value pair concept.
# dicteg={k1:v1,k2:v2,.....kn:vn}
# A dictionary is a collection of items which is ordered, changeable, and does not allow duplicates.
# keys are imutable object (means it can be either a string,numbers,tuple,frozenset), cannot be duplicated,
# values can be mutable and duplicated, can be ANY datatype like numbers, strings, sets, tuples etc

dicteg1={1:"Barath", 2:'John',3:'Ankit'}
print(dicteg1)
dicteg2={
    1:'one',
    2:'Two',
    'Ankit':"Three",
    4:'Four', # With or without comma in ending it works
}

print(dicteg2['Ankit']) # Using key , we can access the value

print(dicteg1.keys()) #output dict_keys([1, 2, 3])
print(dicteg1.values())#outpt dict_values(['Barath', 'John', 'Ankit'])
print(dicteg1.items())#dict_items([(1, 'Barath'), (2, 'John'), (3, 'Ankit')])
dictex={
    'brand':'Audi',
    'model':'q5',
    'year' : 2022,
}

print(dictex['model']) #if u remove quotes and pass model, its error, if there is no quote it will be a variable


person ={
    'id': 4589,
    'name':'John',
    'height': 6.5,
    'languages':['English','Hindi','Spanish',['Python','C','C++','R']],
    'add':('res','off'),
    'M': True,
    'education':{'UG','PG'},
    'comp':4+5j,      
}

print(person['languages'][3][1])
print(type(person['add']))
print(type(person['languages']))
print(type(person['education']))



for key in person.keys():
    print(key)
    
for value in person.values():
    print(value)
    
for key,value in person.items():
    print(key,'  ->  ',value)


    dict1 = {
    1:11,
    2:22,
    3:33,
}

dict2 = {
    4:44,
    5:55,
    6:66,
}

 #print(dict1 +  dict2) 
# 7:77
print(dict2)
dict2[7]=77# adds new key value pair at last
dict2.update({8:'Chethan'})#adds new key value pair at last
print(dict2)
dict2[8]=88
print(dict2)
