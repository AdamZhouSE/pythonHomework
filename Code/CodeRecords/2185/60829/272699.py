def N(xx):
    x= bin(xx+1).replace('0b','')
    res=""
    for i in range(1,len(x)):
        if x[i]=="0":
            res=res+"4"
        else:
            res=res+"7"
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