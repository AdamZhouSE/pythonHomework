n=int(input())
s=input().split(' ')
k=0
result=[]
while k<n:
    min=int(s[k])
    index=k
    for i in range(k+1,n):
        if int(s[i])<min:
            min=int(s[i])
            index=i
    result.append(str(index+1))
    j=0
    while k+j<index-j:
        s[k+j],s[index-j]=s[index-j],s[k+j]
        j=j+1
    k=k+1
re=' '.join(result)
print(re,end=' ')