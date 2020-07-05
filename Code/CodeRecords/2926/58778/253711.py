n=int(input())
s=input()
sl=s.split( )
numlist=[]
for i in sl:
    numlist.append(int(i))
re=[]
for i in numlist:
    temp=[]
    if(len(re)==0):
        temp.append(i)
        re.append(temp)
    else:
        x=0
        for j in re:
            if not(i in j):
                j.append(i)
                x=1
                break
        if(x==0):
            temp.append(i)
            re.append(temp)

print(len(re))