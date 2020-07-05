
arr=input()
size=len(arr)
ans=0
tmp=0
dep=[0]*size
for i in range (size):
    if(arr[i]=='('): 
        tmp+=1
        dep[i]=tmp
    else:
        ans=max(ans,tmp)
        dep[i]=tmp
        tmp-=1
#print(ans)
#print(dep)
out=[0]*size
for i in range (size):
    if(dep[i]>ans/2): out[i]=1
print(out)
#print(arr[0])