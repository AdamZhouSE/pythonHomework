st=input()
s=input()
numlist=eval(s)
uni=[]
for i in numlist:
    temp=[]
    if(len(uni)==0):
        temp.append(i[0])
        temp.append(i[1])
        uni.append(temp)
    else:
        x=0
        for j in uni:
            if(j.count(i[0])!=0):
                j.append(i[1])
                x=1
                break
            elif j.count(i[1])!=0:
                j.append(i[0])
                x=1
                break
        if(x==0):
            temp.append(i[0])
            temp.append(i[1])
            uni.append(temp)
for i in uni:
    i.sort()
    temp=[]
    for j in range(len(i)):
        temp.append(st[i[j]:i[j]+1])
    temp.sort()
    for j in range(len(temp)):
        st=st[0:i[j]]+temp[j]+st[i[j]+1:]
print(st)