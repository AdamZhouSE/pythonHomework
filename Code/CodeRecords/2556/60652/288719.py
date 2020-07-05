n,k=map(int,input().split())
a=[]
for i in range(n):
    x,y=map(int,input().split())
    a.append([x,y])
num,s=0,0
for i in range(n - 1):
    for j in range(i + 1, n):
        if abs(a[i][0] - a[j][0])<k and abs(a[i][1] - a[j][1])<k:
            num+=1
            s= abs(k - abs(a[i][0] - a[j][0])) * abs(k - abs(a[i][1] - a[j][1]))
if num==0:
    print(num)
elif num>1:
    print(-1)
else:
    print(s)