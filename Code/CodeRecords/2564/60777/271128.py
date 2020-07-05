temp=input()
temp=temp[1:len(temp)-1]
temp=[int(x) for x in temp.split(',')]
res=''
count=0
k=int(input())
x=int(input())
index=0
for i in range(len(temp)):
    if(temp[0]>=x):
        index=0
        break
    if(temp[len(temp)-1]<=x):
        index=len(temp)-1
        break
    if(temp[i]<=x and temp[i+1]>x):
        index=i
        break
i=index
j=i+1
while(count<k and i>=0 and j<=len(temp)-1):
    if(abs(temp[i]-x)<=abs(temp[j]-x)):
        if(res==''):
            res+=str(temp[i])
            i-=1
            count+=1
        else:
            res=str(temp[i])+" "+res
            i-=1
            count+=1
    else:
        if(res==''):
            res+=str(temp[j])
            j+=1
            count+=1
        else:
            res+=(" "+str(temp[j]))
            j+=1
            count+=1
        
for m in range(k-count):
    if(i<0):
        res+=(" "+str(temp[j]))
        j+=1
    else:
        res=str(temp[i])+" "+res
        i-=1
res=[int(x) for x in  res.split(' ')]     
print(res)
    
    