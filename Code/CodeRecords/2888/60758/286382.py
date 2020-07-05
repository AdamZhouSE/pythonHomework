m,n=map(int,input().split())
num=list(map(int,input().split()))
for i in range(n):
    l,r=map(int,input().split())
    a=r-l+1
    if(num.count(1)>=a/2 and num.count(-1)>=a/2 and a%2==0):
        print(1)
    else:
        print(0)
    
    