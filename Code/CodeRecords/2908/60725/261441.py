n=int(input())
a=[] 
for i in range(n):
    s=input()
    a.append(s)
for j in range(len(a)):
    a[j]=sorted(a[j])
ans=1
a=sorted(a)
for k in range(1,len(a)):
    if a[k]!=a[k-1]:
        ans+=1
print(ans)        
         
             
        