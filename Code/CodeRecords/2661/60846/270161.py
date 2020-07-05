t=int(input())
while t:
    n=int(input())
    zeros=0
    ones=0
    while n!=0:
        if n%2==1: ones+=1
        else: zeros+=1
        n=n//2
    print(zeros^ones)
    t-=1