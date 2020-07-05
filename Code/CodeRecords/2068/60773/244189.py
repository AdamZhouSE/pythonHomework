n1=int(input())
n2=int(input())
num1=abs(n1)
num2=abs(n2)
sum=0
while(num1>=num2):
    sum=sum+1
    num1=num1-num2

num=n1*n2
if(num<0): sum=0-sum
print(sum)