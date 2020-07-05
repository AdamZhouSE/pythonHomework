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
start=0
end=0
for i in range(len(result)):
    if(result[i]==0):
        ans.append([start+1,end])
        start=i+1
        end=i+1
    else:
        ens=end+1
if(len(ans)==0):
    ans.append([1,max(max_0)])
print(ans)
    
    
    
    
    
    
    
    
    
    
    
    
    