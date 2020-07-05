s=input()
n=len(s)
s="0"+s
res=[]
i=1
while i<=n:
    j,k=i,i+1
    while k<=n and s[j]<=s[k]:
        if s[j]<s[k]:
            j=i
        else:
            j+=1
        k+=1
    while i<=j:
        res.append(i+k-j-1)
        i+=k-j
for i in range(len(res)-1):
    print(res[i],end=" ")
print(res[-1])