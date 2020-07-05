from itertools import combinations_with_replacement as cwr
n=int(input())
m=int(input())
sources=[1,2,3,4]
lists=[]
for i in range(n):
    lists.append(0)
target=list(cwr(sources,r=m))
res=[]
for i in target:
    a=lists.copy()
    for x in i:
        if(x==1):
            for y in a:
                if(y==0):
                    y=1
                else:
                    y=0
        elif(x==2):
            for y in range(len(a)):
                if(y%2==1):
                    if(a[y]==0):
                        a[y]=1
                    else:
                        a[y]=0
        elif(x==3):
            for y in range(len(a)):
                if(y%2==0):
                    if(a[y]==0):
                        a[y]=1
                    else:
                        a[y]=0
        elif(x==4):
            for y in range(len(a)):
                if(y%3==0):
                    if(a[y]==0):
                        a[y]=1
                    else:
                        a[y]=0
    if(not a in res):
        res.append(a)
print(len(res))