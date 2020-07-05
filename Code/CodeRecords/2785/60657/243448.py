import re
up=input()
up=int(up)
con=[]
for i in range(up):
    a=input()
    a=int(a)
    con.append(a)
con.sort()
if(sum(con)%360==0):
    cons='YES'
else:
    temp=[]
    for i in range(len(con)):
        if con.count(con[i])%2!=0:
            temp.append(con[i])
    if (len(temp)==0):
        cons='YES'
    elif(sum(con[0:-1])==con[-1]):
        cons='YES'
    else:cons='NO'
print(cons)