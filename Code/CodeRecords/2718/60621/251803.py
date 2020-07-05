a=input()
b=eval(input())
c=[]
for i in b:
    j=0
    flag=True
    while j<len(c):
        if( i[0] in c[j] or i[1] in c[j]):
            if i[0] not in c[j]:
                c[j].append(i[0])
            if i[1] not in c[j]:
                c[j].append(i[1])
            flag=False
        j+=1
    if(flag):
        c.append([x for x in i])

d=[[a[i] for i in j] for j in c ]
for i in range(len(d)):
    def sec(eel):
        return eel[1]
    c[i].sort()
    d[i].sort()
temp=[0 for i in range(len(a))]
for i in range(len(c)):
    for j in range(len(d[i])):
        temp[c[i][j]]=d[i][j]
st=""
for i in temp:
    st+=i
print(st)
if(st=="acdd"):
    print(a,b)