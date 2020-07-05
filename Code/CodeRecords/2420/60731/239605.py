num=int(input())
num1=num
num2=0
for i in range(1,num):
    num1=num-i
    num2=i
    if '0' not in str(num1) and '0' not in str(num2):
        print([num2,num1])
        break