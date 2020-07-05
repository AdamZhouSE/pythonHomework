x=input().split()
num=int(x[0])
k=int(x[1])
name=[]
age=[]
x=input().split()
name.append(x[0])
age.append(int(x[1]))
for i in range(1,num):
    x=input().split()
    tmp=x[0]
    Tage=int(x[1])
    for j in range(i-1,-1,-1):
        if Tage!=age[j]:
            tmp+=name[j]
            break
    name.append(tmp)
    age.append(Tage)
#print(name)
res=[]
for i in range(k):
    tag=input()
    tmp=0
    l=len(tag)
    for j in name:
        if l<=len(j):
            #print(j)
            if j[0:l]==tag:
                tmp+=1
    res.append(tmp)
#print(res)
for i in res:
    print(i)
    