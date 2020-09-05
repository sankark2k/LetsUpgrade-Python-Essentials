#1. IF ELSE

altitude = int(input('Enter altitude value - '))
if altitude<=1000 :
    print('Safe to Land')
elif altitude>1000 and altitude <=5000 :
    print('Bring down to 1000')
elif altitude>5000 :
    print('Turn Around')








#2. print all PRIME NUMBERS in range of 1 to 200

for num in range(1,200):
    if num>1:
        for i in range(2,num):
            if(num % i) ==0:
                break
        else:
            print(num)
