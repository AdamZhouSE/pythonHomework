n=int(input())
cordlist=[]
for i in range(n):
    m=input()
    ml=m.split( )
    temp=[]
    temp.append(int(ml[0]))
    temp.append(int(ml[1]))
    cordlist.append(temp)
re=[]
for i in cordlist:
    temp=[]
    if(len(re)==0):
        temp.append(i)
        re.append(temp)
    else:
        for j in re:
            k=0
            for x in j:
                if(x[0]==i[0] or x[1]==i[1]):
                    j.append(i)
                    k=1
                    break
            if(k==1):
                break
        if(k==0):
            temp.append(i)
            re.append(temp)
print(len(re)-1)
