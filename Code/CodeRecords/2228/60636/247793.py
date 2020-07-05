target=int(input())
sum=0
n=0
target=abs(target)
while(1):
    if (sum>=target):
        if(sum==target)|((sum-target)%2== 0):
            print(n)
            break
        elif(n%2==0):
            print(n+1)
            break
        else:
            print(n+2)
            break
    n=n+1    
    sum=sum+n