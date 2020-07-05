from itertools import combinations_with_replacement as cwr
n=int(input())
m=int(input())
print(n)
print(m)
sources=[1,2,3,4]
lists=[]
for i in range(n):
    lists.append(0)
target=list(cwr(sources,r=m))
print(target)
res=[]
for i in target:
    for x in i:
        if(x==1):
            for y in lists:
                if(y==0):
                    y=1
                else:
                    y=0
        elif(x==2):
            for y in range(len(lists)):
                if(y%2==1):
                    if(lists[y]==0):
                        lists[y]=1
                    else:
                        lists[y]=0
        elif(x==3):
            for y in range(len(lists)):
                if(y%2==0):
                    if(lists[y]==0):
                        lists[y]=1
                    else:
                        lists[y]=0
        elif(x==4):
            for y in range(len(lists)):
                if(y%3==0):
                    if(lists[y]==0):
                        lists[y]=1
                    else:
                        lists[y]=0
    if(not lists in res):
        res.append(lists)
print(len(res))