m,n=map(int,input().split())
num=list(map(int,input().split()))
for i in range(n):
    l,r=map(input().split())
    a=r-l+1
    if(num.count(1)>=a and num.count(-1)>=a and a%2==0):
        print(1)
    else:
        print(0)