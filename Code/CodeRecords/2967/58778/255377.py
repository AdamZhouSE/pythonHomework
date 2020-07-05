n=int(input())
strlist=[]
lenlist=[]
for i in range(n):
    s=input()
    strlist.append(s)
    lenlist.append(len(s))
x=min(lenlist)
index=lenlist.index(x)
temp=[]
for i in range(x):
    j=0
    t=0
    while(j<x):
        j=x-i+t
        temp.append(strlist[index][t:j])
        t=t+1
for c in temp:
    x=0
    for j in strlist:
        if not(c in j):
            x=1
            break
    if(x==0):
        print(len(c))
        break