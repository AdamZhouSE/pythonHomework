t=int(input())
for i in range(t):
    n,money=map(int,input().split())
    result=0
    if n%2==0:
        result=(n//2)*money
    else:
        result=((n+1)//2)*money
    print(result)