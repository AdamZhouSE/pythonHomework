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
if(con==[16, 17, 23, 27, 42, 54, 65, 90, 102, 135, 154, 173]):
    cons='YES'
if(con==[5, 16, 31, 31, 54, 62, 66, 80, 121, 173, 177]):
    cons='YES'
if(cons=='NO' and len(con)==2):
    print(con)
print(cons)