#QUESTION-1
# Decorator

def getInput(calculate_arg_fun):
    
    def wrap_function():
    
        a = int(input("Enter First Number - "))
        
        b = int(input("Enter Second Number - "))
        
        calculate_arg_fun(a,b)   
    
    return wrap_function
# calling decorator for input

@getInput

def EvenFinder(start, last):
    
    print("The Even numbers in the range",start,"to",last,"is :")

    for n in range(start, last + 1): 
      
        if n % 2 == 0:             
            print(n, end = " ")
EvenFinder()


#
print(' ')
print(' ')
print(' ')
print(' ')
#

#QUESTION-2
#Handling the exception
%%writefile test.txt
Hi this is sankar 
i love python


# opening file in read mode and trying to write 

try:
    
    file = open("test.txt","r")
    
    file.write("I am from salem.")
    
    print("Write operation has done successfully in read only mode.")
    
except Exception as e:
    
    print("Error has been occured")
    
    print("Error message is :",e)
