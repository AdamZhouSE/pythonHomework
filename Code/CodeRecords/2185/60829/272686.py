def N(x):
    res=""
    while not x==0:
        if x%2==1:
            if  not res==" ":
                res=res+"7"
        else:
            res=res+"4"
        x=(x-x%2)//2
    return res    
a=int(input())
aa=[]
for i in range(0,a):
    aa.append(int(input()))
res=[]
for i in range(0,a):
              res.append(N(aa[i]))
for i in range(0,a):
              print(res[i])