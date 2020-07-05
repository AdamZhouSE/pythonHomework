guest=int(input())
hi=[0]*guest
mi=[0]*guest
table=[[0 for i in range(2)] for j in range(guest)]
temp=[]
for i in range(guest):
    line=input().split()
    hi[i]=int(line[0])
    mi[i]=int(line[1])
for k in range(guest):
    table[k]=[hi[k],mi[k]]
for q in range(guest):
    temp.append(table.count(table[q]))
res=max(temp)
print(res)