n=int(input())
x=100
num=0
for i in range(n):
    a,p=map(int,input().split())
    x=min(x,p)
    num+=a*x
print(num)