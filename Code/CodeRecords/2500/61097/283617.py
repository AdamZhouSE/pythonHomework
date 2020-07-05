import re

arr=input()
#a=[0]
b=re.findall(r'\d+',arr)
b=list(map(int,b))
a=[0]*(len(b)+1)
#print(a)
for i in range(1,len(b)+1): a[i]=b[i-1]
#print(a)
size=len(a)-1
ans=[0 for i in range(2*size-2)]
tmp=[0 for i in range(size+1)]
for i in range(1,size+1):
    tmp[a[i]]=i
#print(tmp)
i=0
while i<size-1:
    ans[2*i]=tmp[size-i]
    #print(ans[2*i])
    ans[2*i+1]=size-i
    for j in range(1,size+1):
        if(tmp[j]<=ans[2*i]): tmp[j]=ans[2*i]-tmp[j]+1
    for j in range(1,size+1): 
        if(tmp[j]<=size-i): tmp[j]=size-i+1-tmp[j]
    #print(tmp)
    i+=1
#print(tmp)
ans.remove(1)
print(ans)
