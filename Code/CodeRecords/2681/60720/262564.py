size=int(input())
for i in range(size):
    count=0
    n=int(input())
    while n>0:
        if n%2==0:
            n=n//2
            count+=1
        else:
            n-=1
            count+=1
    print(count)