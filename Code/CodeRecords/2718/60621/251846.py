a=input()
b=eval(input())
c=[]
for i in b:
    j=0
    flag=True
    while j<len(c):
        if( i[0] in c[j] or i[1] in c[j]):
            if i[0] in c[j] and i[1] in c[j]:
                c[j].append(i[0])
                c[j].append(i[1])
            if i[0] not in c[j]:
                flag2=True
                k=j+1
                while k<len(c):
                    if i[0] in c[k]:
                        c[j]=c[j]+c[k]
                        c.pop(k)
                        flag2=False
                        break
                    k+=1
                if flag2:
                    c[j].append(i[0])

            if i[1] not in c[j]:
                flag2 = True
                k = j + 1
                while k < len(c):
                    if i[1] in c[k]:
                        c[j] = c[j] + c[k]
                        c.pop(k)
                        flag2 = False
                        break
                    k += 1
                if flag2:
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