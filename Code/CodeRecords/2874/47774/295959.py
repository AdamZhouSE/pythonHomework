n=int(input())
ss=input()
a=[int(i) for i in ss.split(' ')]
num=0
for i in range(n-1):
    if a[i]==0:
        num+=1
    elif a[i]==1:
        if a[i+1]==1:
            a[i+1]=0
        elif a[i+1]==3:
            a[i+1]=2
    elif a[i]==2:
        if a[i+1]==2:
            a[i+1]=0
        elif a[i+1]==3:
            a[i+1]=1
if a[n-1]==0:
    num+=1
print(num)
        