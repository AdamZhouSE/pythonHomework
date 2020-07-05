s=input()
s=s[1:len(s)-1]
sl=s.split(',')
airport=[]
i=0
while i <len(sl):
    temp=[]
    j=i
    for j in range(j,j+2):
        if (sl[j][0:1] == '['):
            sl[j] = sl[j][2:len(sl[j])-1]
            temp.append(sl[j])
        elif (sl[j][len(sl[j])-1:len(sl[j])]==']' and sl[j][0:1] == ' '):
            sl[j] = sl[j][2:len(sl[j]) - 2]
            temp.append(sl[j])
        elif (sl[j][len(sl[j])-1:len(sl[j])]==']'):
            sl[j] = sl[j][1:len(sl[j]) - 2]
            temp.append(sl[j])
        else:
            sl[j] = sl[j][3:len(sl[j]) - 1]
            temp.append(sl[j])
    i=i+2
    airport.append(temp)
rout=[]
#print(airport)
f='JFK'
rout.append(f)

while len(rout)!=len(airport)+1:
    temp=[]
    for  i in range(len(airport)):
        if(airport[i][0]==f):
            x=rout.count(f)
            if(x!=0):
                x=rout.index(f)
            if(x==len(rout)-1):
                temp.append(airport[i][1])
            else:
                if(airport[i][1]!=rout[x+1]):
                    temp.append(airport[i][1])
    if(len(temp)==0):
        print(s)
        break
    else:
        rout.append(min(temp))
        f=min(temp)
print(rout)
#print(airport)