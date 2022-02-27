name = 'Chethan'
print(len(name))
print(name[4])

print("**********Slicing**********")

str1 = 'Donald'
print(str1[2:5]) # str[si:li] . It Prints from si to li-1 . O/p - nal

print(str1[2:15]) # Even if you give last index value greater thn length of string. 
                    #It will give output untill end of string. O/p - nald


str2 ='Donald Trump'
print(str2[2:7])

str3 = "Chethan"
print(str3[::2]) # str[si:li:stepvalue]. Stepvalue by default is 1. 
                   #If u give any value(suppose 2 is step value), it will print from si to li , by printing every 2nd character  one after the other

print(str2[::]) #It prints entire string
print(str2[:5]) #It prints from 0 to 4

'''
Default value for si: 0
Default value for li: len(string)
Default value for stepvalue is : 1
'''

print("**********Negative-Slicing**********")

name = 'Barath'
print(name[-1:-4:1]) #It wont print anything

print(name[-4:-1:1]) #rat
print(name[:-3:-1]) # It will print last n+1 charcters. In th ex,it will print last last 2 character.
print(name[:3:-1])


