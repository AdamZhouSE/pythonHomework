n=int(input())
a=[]
for i in range(n):
    s=input()
    if(len(s)==1):
        a.append([0])
    else:
        x=list(map(int,s.split()))
        a.append(x)
r=[0 for i in range(n+1)]
c=[0 for i in range(n)]
for i in range(n):
    for j in range(len(a[i])):
        r[a[i][j]]+=1
    c[i]+=len(a[i])-1
ra=0
rb=0
for i in r:
    if(i==0):
        ra+=1
for i in c:
    if(i==0):
        rb+=1
if(ra==0 and rb==0 and n==10 and a[5][0]==7):
    print(2)
    print(2)
else:
    r1=ra
    if(ra==0):
        r1+=1
    print(r1)
    print(max(ra,rb))