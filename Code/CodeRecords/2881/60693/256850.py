def crystal(n):
    res=[]
    for i in range(1,n,2):
        str="*"*((n-i)//2)+"D"*i+"*"*((n-i)//2)
        res.append(str)
    res.append('D'*n)
    for i in range((n-1)//2-1,-1,-1):
        res.append(res[i])
    return res

n=int(input())
cry=crystal(n)
for x in cry:print(x)