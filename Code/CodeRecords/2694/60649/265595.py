s=input()
n=len(s)
max1=-1
res=[]
for i in range(n-1):
    for j in range(i+1,n):
        k=0
        while j+k<n and  s[i+k]==s[j+k]:
            k+=1
        if k>max1 and k!=0:
            max1=k
            res=[s[i:i+k]]
        elif k==max1:
            res.append(s[i:i+k])
if len(res)==0:
    print("")
else:
   for r in res:
       print(r)