#To print 1st ARMSTRONG NUMBER in range

for num in range(1042000,702648265):
    sum = 0
    n=len(str(num))
    temp = num
    while temp>0:
        digit=temp%10
        sum +=digit**n
        temp //=10
    if num == sum:
        print('The first ARMSTRONG number - ',num )
        break


