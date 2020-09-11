#QUESTION 1
#To check sublist [1,1,5] in a list as same order
lst = [1, 1, 5]

lst1 = []

l = int(input("\nEnter the length of the list : "))

j = 0;

# creating a list from user value

for i in range (0,l):

    lst1.append(int(input("\nEnter the number for the list : ")))

print()

print("List is : ", lst1)

for i in range(0,l):
    
    if( lst1[i] == lst[j] ):
        
        j += 1
        
        i += 1
        
    else:
        
        i +=1
    
if( j == 3 ):

    print ("It's a match")

else:
    print ("It's Gone")
#

print(" ")
print(' ')
print(' ')

#

#QUESTION 2
#Make a function for prime numbers and use filter to filter out all the prime numbers from 1-2500

def filterPrime(num):
    for i in range(2,num):
        if num%i ==0:
            return False
        else:
            return True

#Declare filter function
primeNum = filter(filterPrime, range(2500+1))
#Print the list of Prime numbers
print(list(primeNum))


#
print(' ')
print(' ')
print(' ')
#

#QUESTION 3
# Make a Lambda function for capitalizing the whole sentence passed using arguments.
# And map all the sentences in the List, with the lambda functions

lst = ["hey this i sankar","i am from salem"]

print("Original list : ")

print(lst)

capList = list(map(lambda words: " ".join([word.capitalize() for word in words.split( )]) ,lst))

print("Capitalized list is : ")

print(capList)

