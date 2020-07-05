nums=input()
nums=nums.lstrip('[')
nums=nums.rstrip(']')
num=nums.split(',')
num0=0
num1=0
num2=0
for item in num:
    if item=='0':
        num0=num0+1
    elif item=='1':
        num1=num1+1
    else:
        num2=num2+1
for i in range(len(num)):
    if i<num0:
        num[i]=0
    elif i<num0+num1:
        num[i]=1
    else:
        num[i]=2
print(num)