n=int(input())
count=0
for i in range(2,n+1):
    for j in range(2,int(n**0.5)+1):
        if i%j==0:
            count+=1
sum=0
for i in range(1,count+1):
    sum=sum*i*(n-i)
if n==1 or n==2:
    print(1)
else:
    print(sum%(10**9)+7)
