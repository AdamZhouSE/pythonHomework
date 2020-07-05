n=list(input())
n=[int(i) for i in n]
a=sorted(n,reverse=True)
result=[]
if(a==n):
    result.extend(n)
else:
    if(n[0]!=max(n)):
        index=n.index(max(n))
        n[0],n[index]=n[index],n[0]
        result.extend(n)
    else:
        for i in range(1,len(n)):
            if(n[i]==max(n[i:n])):
                continue
            else:
                index=n.index(max(n[i:n]))
                n[i],n[index]=n[index],n[i]
                result.extend(n)
                break
result=[str(i) for i in result]
print(''.join(result))
        
