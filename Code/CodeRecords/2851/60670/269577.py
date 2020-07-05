n=int(input())
edge=0
for i in range(0,n):
    x,y=map(int,input().split())
    if x+y>edge:
        edge=x+y
print(edge)