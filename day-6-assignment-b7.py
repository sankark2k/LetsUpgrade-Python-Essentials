#QUESTION-1
#class for BANK ACCOUNT
class BankAccount: 

    def __init__(self): 

        self.ownerName="SANNKAR"
        
        self.Balance=0
        
    def deposit(self): 
        
        Amount=float(input("Enter amount to be Deposited : ")) 
        
        self.Balance += Amount 
        
        print("Amount Deposited is :",Amount) 
  
    def withdraw(self): 
        
        Amount = float(input("Enter amount to be Withdrawn : ")) 
        
        if self.Balance >= Amount: 
        
            self.Balance -= Amount 
            
            print("You have Withdrew :", Amount) 
        
        else: 
        
            print("Insufficient balance in the account...") 

print("---WELCOME TO BACK ACCOUNT PROGRAM---")
    
BA = BankAccount()

print("Account Holder Name is :",BA.ownerName)
    
print("Initial Account Balance is :",BA.Balance)
   
BA.deposit();
    
BA.withdraw();
    
print("Net Avaliable balance is : ",BA.Balance)



#QUESTION-2
#PROGRAM FOR CONE'S VOLUME AND SURFACE AREA

import math

pi = math.pi

class cone:
    
    def __init__(self,r,h): 

        self.r=r
        
        self.h=h
        
    def volume(self):
        
        result = (1 / 3) * pi * self.r * self.r * self.h
        
        print("\nVolume Of Cone is :",result)
        
    def surfacearea(self):
        
        result = pi * self.r * self.h + pi * self.r * self.r
         
        print("\nSurface Area Of Cone is :",result)

ra = float(input("\nEnter the radius of cone : "))

he = float(input("\nEnter the height of cone : "))

c = cone( ra, he)

c.volume()

c.surfacearea()
