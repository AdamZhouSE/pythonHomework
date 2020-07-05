data=list(input().split(" "))
num=list(input().split(" "))
num1=0
for i in range(int(data[0])):
    num[i]=int(num[i])
for i in range(int(data[0])-1):
    while (num[i]>=num[i+1]):
        num[i+1]=num[i+1]+int(data[1])
        num1=num1+1
print(num1)