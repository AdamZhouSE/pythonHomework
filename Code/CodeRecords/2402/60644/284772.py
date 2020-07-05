n=int(input())
res=[]
a=[]
for i in range(0,n):
    a=a+[input().split(',')]
t=int(input())
for i in range(0,n):
    for j in range(0,len(a[i])):
        a[i][j]=int(a[i][j])
res=[0]*t
for i in range(0,n):
    for j in range(a[i][0],a[i][1]+1):
        res[j-1]=res[j-1]+a[i][2]
print(res)
