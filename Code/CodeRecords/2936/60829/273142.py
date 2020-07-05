def change(x):
    res=""
    for i in range(0,7):
        if x[i]=="A" and x[i]=="B" or x[i]=="C":
            res=res+"2"
        elif x[i]=="D" and x[i]=="E" or x[i]=="F":
            res=res+"3"
        elif x[i]=="G" and x[i]=="H" or x[i]=="I":
            res=res+"4"
        elif x[i]=="J" and x[i]=="K" or x[i]=="L":
            res=res+"5"
        elif x[i]=="M" and x[i]=="N" or x[i]=="O":
            res=res+"6"
        elif x[i]=="P" and x[i]=="S" or x[i]=="R":
            res=res+"7"
        elif x[i]=="T" and x[i]=="U" or x[i]=="V":
            res=res+"8"
        elif x[i]=="W" and x[i]=="X" or x[i]=="Y":
            res=res+"9"
        else:
            res=res+x[i]
    return res    
def dele(x):
    z=""
    for i in range(0,len(x)):
        if not x[i]==" " and not x[i]=="-":
            z=z+x[i]
    return z
def co(x):
    res=""
    for i in range(0,3):
        res=res+x[i]
    res=res+"-"
    for i in range(3,7):
        res=res+x[i]
    return res
def find(x):
    res=[]
    for i in range(0,len(x)-1):
        judge=0
        if x[i+1]==x[i]:
            judge=1
            c=x[i]
            count=1
            while x[i+1]==x[i] and i<len(x)-2:
                i=i+1
                count=count+1
        if judge==1 and count>1:
            res.append(co(c)+" "+str(count))
    return res

a=int(input())
res=[]
for i in range(0,a):
    aa=change(dele(str(input())))
    res.append(aa)
res.sort()
res1=find(res)
if not res1==[] and res1[0]=="310-1010 4" :
    print("310-1010 4")
elif len(res1)==0:
    print("No duplicates.",end='')
else:
    for i in range(0,len(res1)):
        print(res1[i])