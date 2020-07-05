k=int(input())
n=int(input())
result=range(n+1)
for i in range(2,k+1):
    r=[0]
    x=1
    for j in range(1,n+1):
        while(x<j and max(result[x-1],r[j-x])>max(result[x],r[j-x-1])):
            x+=1
        r.append(1+max(result[x-1],r[j-x]))
    result=r
print(result[-1])