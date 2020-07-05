temp=input()
temp=temp[1:len(temp)-1]
al=[]
for i in range(len(temp)):
    if(temp[i]=='['):
        j=i
        while(temp[j]!=']'):
            j+=1
        now=[int(x) for x in temp[i+1:j].split(',')]
        al.append(now)
        
for i in al:
    for j in al:
        if(j!=i):
            if(not(j[0]>i[1] or j[1]<i[0])):
                i[0]=min(i[0],j[0])
                i[1]=max(i[1],j[1])
                al.remove(j)
                
print(al)