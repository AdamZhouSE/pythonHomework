k=int(input())
lst=list(map(int,input().split(',')))
count=0
num=2

while count<k-1:

    n=num
    for i in lst:
        while n%i==0:
            n=n/i
    num+=1
    if n==1:count+=1
print(num-1)