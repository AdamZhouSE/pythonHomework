temp=input()
temp=temp[1:len(temp)-1]
temp=[int(x) for x in temp.split(',')]
res=temp.copy()
res.sort()
group=[]
find=False
def divide(li,k,ind,n):
    if(k==0):
        group.append(ind.copy())
        return 
    if(k==1):
        group.append(ind.copy())
        return
    if(k==2):
        for i in range(n+1,len(li)):
            ind.append(i)
            divide(li,0,ind,len(li))
            ind.remove(i)
        return
    if(k>2):
        for i in range(n+1,len(li)-k+2):
            ind.append(i)
            divide(li,k-1,ind,i)
            ind.remove(i)
        return
for i in range(len(temp),0,-1):
    group=[]
    divide(temp,i,[],0)
    for x in group:
        if(x==[]):
            print(1)
            find=True
            break
        pre=[]
        for j in range(len(x)):
            if(j==0):
                get=temp[:x[j]]   
            else:
                get=temp[x[j-1]:x[j]]
            get.sort()
            pre+=get
        get=temp[x[len(x)-1]:]
        get.sort()
        pre+=get
        if(pre==res):
            print(i)
            find=True
            break
    if(find):
        break