def so(x,num):
    if len(x)==1:
        return num
    x = sorted(x)
    ml=0
    temp = x[0]
    zz=0
    res=[]
    for i in x:
        temp=0
        for j in x:
            if i==j:
                temp+=1
        res.append(temp)
    return sorted(res)[-1]
            
num = int(input())
x=input().split(' ')
x=list(map(int,x))
print(so(x,num))