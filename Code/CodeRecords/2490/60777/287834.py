t1=input()
t1=t1[1:len(t1)-1]
t1=[int(x) for x in t1.split(',')]
t2=input()
t2=t2[1:len(t2)-1]
t2=[int(x) for x in t2.split(',')]
res=[]
i=0
while(i<len(t1)):
    if(t1[i] in t2):
        res.append(t1[i])
        t2.remove(t1[i])
        del t1[i]
        i-=1
    i+=1
    
res.sort()
print(res)