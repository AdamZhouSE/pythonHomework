n=eval(input())
sum1=0
for i in range(1,n//2+1):
    if n%i==0:
        sum1+=i
print(n==sum1)