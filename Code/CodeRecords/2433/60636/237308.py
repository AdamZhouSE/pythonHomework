list=input("")[1:-1].split(",")
source=[]
for i in range(int(len(list)/2)):
    a=[]
    a.append(int(list[2*i][1:]))
    a.append(int(list[2*i+1][:-1]))
    source.append(a)
max_0=[]
for i in range(len(source)):
    max_0.append(max(source[i]))
result=[]
for i in range(max(max_0)):
    result.append(0)
for i in range(len(source)):
    for a in range(source[i][0]-1,source[i][1]):
        result[a]=1
ans=[]
start=1
end=0
for i in range(len(result)):
    if(0 in result[start:i]):
        if(i-1!=start):
            ans.append([start,i-1])
        start=i+1
if(result[-1]==1):
    if(start==1):
        start=0
    ans.append([start+1,max(max_0)])
print(ans)
    
    
    
    
    
    
    
    
    
    
    
    
    