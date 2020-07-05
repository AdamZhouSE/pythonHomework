n=int(input())
num=0
i=1
while(n>num+i*9*10**(i-1)):
    num+=i*9*10**(i-1)
    i+=1
a=10 **(i-1)-1+(n-num)//i
b=(n-num)%i
if b==0:
    result=a%10
else:
    a+=1
    result=(a//10**(i-b))%10
print(result)