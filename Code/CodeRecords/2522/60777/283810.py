temp=input()
temp=temp[1:len(temp)-1]
a1=[int(x) for x in temp.split(',')]
temp=input()
temp=temp[1:len(temp)-1]
a2=[int(x) for x in temp.split(',')]
ind=0
for i in range(len(a2)):
    pre=a2[i]
    for j in range(ind,len(a1)):
        if(a1[j]==pre):
            get=a1[ind]
            a1[ind]=a1[j]
            a1[j]=get
            ind+=1
un=a1[ind:]
un.sort()
res=a1[:ind]+un

print(res)