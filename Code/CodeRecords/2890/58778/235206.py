str1=input()
strlist1=str1.split( )
numofte=int(strlist1[0])
x0=int(strlist1[1])
y0=int(strlist1[2])
colist=[]
for i in range(numofte):
    s=input()
    str2=s.split( )
    temp=[]
    temp.append(int(str2[0])-x0)
    temp.append(int(str2[1])-y0)
    colist.append(temp)
cplist=colist.copy()
for i in range(len(colist)-1):
    if (colist[i][0]!=0 and colist[i][1]!=0):
        for j in range(i+1,len(colist)):
            if(colist[j][0]/colist[i][0]==colist[j][1]/colist[i][1]):
                cplist[j]=[0,0]
    elif colist[i][0]==0:
        for j in range(i+1,len(colist)):
            if(colist[j][0]==0):
                cplist[j]=[0,0]
    elif colist[i][1]==0:
        for j in range(i+1,len(colist)):
            if(colist[j][1]==0):
                cplist[j]=[0,0]
print(len(cplist)-cplist.count([0,0]))
