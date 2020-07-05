temp=input()
temp=temp[1:len(temp)-1]
li=[int(x) for x in temp.split(',')]
res=[]
for i in range(len(li)):
    count=0
    for j in range(i+1,len(li)):
        if(li[j]<li[i]):
            count+=1
    res.append(count)
    
print(res)