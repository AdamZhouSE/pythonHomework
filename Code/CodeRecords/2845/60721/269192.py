n=int(input())
a=[]
b=[]
for i in range(0,n):
    q,p=(map(int,input().split(' ')))
    a.append(q)
    b.append(p)
al=False
for i in range(0,n-1):
    for j in range(i+1,n):
        if((a[i]-a[j])*(b[i]-b[j])<0):
            al=True
if(al==True):
    print('Happy Alex')
else:
    print('Poor Alex')
