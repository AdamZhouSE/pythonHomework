n,d=map(int,input().split())
b=list(map(int,input().split()))
num=0
for i in range(n-1):
    x=max(0,(b[i]-b[i+1])//d+1)
    b[i+1]+=d*x
    num+=x
print(num)