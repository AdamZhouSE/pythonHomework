temp=input()
temp=temp[1:len(temp)-1]
temp=[int(x) for x in temp.split(',')]
res=0
for i in range(len(temp)):
    for j in range(i+1,len(temp)):
        if(temp[i]>2*temp[j]):
            res+=1
            
print(res)