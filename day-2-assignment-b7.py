#Assignment 1 - DAY 2
#Work with default functions of each one of data type (list, dict, set, tuple and string)


#1. LIST and its default functions 
print('...#LIST...')
lst = ['sankar', 10, 12001, 25.49, 'Hello']
print(lst)
lst.append(12.0) #to add new element in a list
print(lst)
print('index value of 10 is ',lst.index(10)) # to find index value of element
print(lst[-1]) # access element using index value
lst.insert(1,['hi', 1]) # insert new element in a particular index
print(lst)
lst.remove(lst[2]) #to remove particular element in a list      
print(lst)
lst.clear() #to clear all the elements in a list and make it is as empty list
print(lst)


#2. DICTIONARY and its default functions
print('...#DICTIONRY...')
dit={'name':'sankar', 'age': 20, 'place':'salem', 'mob_num':88259}
print(dit)
print('age is ',dit.get('age')) #accessing a particular value using GET method

print(dit.keys()) #it displays a keyvalues of dictionary

dit.pop('place') #remove particular element 
print(dit)

dit.update({'clg':'avs'}) #adding new value in a dictionary
print(dit)

dit1 = dit.copy() #copy complete dictionary to some other dictionary
print(dit1)


#3. SET and its default functions/methods
print('...SET...')

set1={1,2,3,'sankar',2.5}
print(set1)

set1.add('hello') #add new element in set
print(set1)

set1.update(['salem', 321, 25.0]) #updating elements in a set
print(set1)

set1.remove(2) #remove particular element
print(set1)

set2 = {1,2,'world', 3.7}
set3=set2.union(set1) #join two sets
print(set3)

set3=set2.difference(set1) #remove common elements on both sets and print remaining
print(set3)


#4. TUPLES and its default methods
print('...TUPLES...')

tup = (1,2,3,4,5,4,2,4,3,3,5,6,7,8,3, '@')
print(tup)

#count the value in tuple
print('how many times the value 3 present in a tuple ', tup.count(3))

#find index of value
print('index of value @ is ', tup.index('@'))

tup1= ('san')
tup2=('kar')
tup3=tup1 + tup2 #adding two tuples into one tuple
print(tup3) 

print(tup[6])
print(tup[9:])

#5. STRINGS and explore its functions
print('...STRING...')

string = '  Hii all, this is one of the sentence'
print(string.strip()) #it removes white spaces at begining or at end
str1="HELLO WORLD - small letters" 
print(str1.lower()) #convert upper to lower case
str2="hello world - capital letters"
print(str2.upper()) #convert lower to upper case
print(string.replace('sentence','replaced sentence')) #replace particular word
print(string.split(',')) #it split the string 
