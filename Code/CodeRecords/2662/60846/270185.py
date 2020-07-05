def NumOfOne(n):
    ones=0
    while n!=0:
        if n%2==1: ones+=1
        n=n//2
    if ones%2==1: print('odd')
    else: print('even')
t=int(input())
while t:
    n=int(input())
    NumOfOne(n)
    t-=1