s=input()
s=' '+s
leng=len(s)
i=1
res=[]
while(i<leng):
    j=i
    k=i+1
    while(k<leng and s[j]<=s[k]):
        if(s[j]<s[k]):
            j=i
        else:
            j+=1
        k+=1
    while(i<=j):
        res.append(str(i+k-j-1))
        res.append(" ")
        i+=k-j
res.pop()
print("".join(res))
