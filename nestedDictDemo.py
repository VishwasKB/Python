# one way of defining dict with dict 
myFamily = {
    'child1' :{
        'name':'Emily',
        'year':2004,
    },
    'child2' : {
        'name':'John',
        'year' : 2014,
        
    },
    'child3' :{
        'name' :"Mark",
        "year" : 2021,
    },
}

print (myFamily['child3']['year']) 

print("Second way ======")

child1 ={
        'name':'Emily',
        'year':2004,
}

child2 ={
        'name':'John',
        'year' : 2014,
}

child3 ={
        'name' :"Mark",
        "year" : 2021,
}

myFamily1 = {
    "child1":child1,
    'child2':child2,
    'child3':child3,
    
}

print(myFamily1['child3']['name'])