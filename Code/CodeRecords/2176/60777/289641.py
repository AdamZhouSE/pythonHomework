s=input()
end=[]
ind=[]
for i in range(len(s)-1,-1,-1):
    end.append(s[i:])
    ind.append(i+1)
    
for i in range(len(end)-1):
    for j in range(len(end)-1-i):
        m=0
        pre=end[j]
        it=end[j+1]
        while(m<len(end[j]) and m<len(end[j+1])):
            if(it[m]<pre[m]):
                temp=end[j]
                end[j]=end[j+1]
                end[j+1]=temp
                temp=ind[j]
                ind[j]=ind[j+1]
                ind[j+1]=temp
                break
            m+=1
        if(pre.find(it)!=-1):
                temp=end[j]
                end[j]=end[j+1]
                end[j+1]=temp
                temp=ind[j]
                ind[j]=ind[j+1]
                ind[j+1]=temp

for i in range(len(ind)):
    if(i!=len(ind)-1):
        print(ind[i],end=' ')
    else:
        print(ind[i])