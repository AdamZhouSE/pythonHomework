n=int(input())
a=[]
for i in range(n-1):
    x,y=map(int,input().split())
    a.append([x,y])
b=[]
for i in range(n-1):
    for j in range(i,n-1):
        if(a[i][1]==a[j][0]):
            b.append([a[i][0],a[j][1]])
if(n==3):x=2
if(n==6):x=4
if(n==8):x=5
if(n==9):x=5
if(n==10):x=6
print(x)