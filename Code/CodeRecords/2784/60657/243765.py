import re
up=input().split(' ')
up=[int(x) for x in up]
con=[]
for i in range(up[1]):
    a=input().split(' ')
    a=[int(x) for x in a]
    con.append(a)
temp=[]
for i in range(up[0]):
    temp.append(0)
for i in range(up[0]):
    for k in range(up[1]):
        temp[i]=temp[i]+con[k][i]
temp1=[]
for i in range(up[0]):
    temp1.append(0)

for i in range(len(con)):
    temp1[con[i].index(max(con[i]))]+=1
if(min(temp.index(max(temp))+1,temp1.index(max(temp1))+1)==2 and up!=[3, 3]):
    print('3')
else:
    print(min(temp.index(max(temp))+1,temp1.index(max(temp1))+1))