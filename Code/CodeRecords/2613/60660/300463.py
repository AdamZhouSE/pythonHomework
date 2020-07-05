import re
n=int(input())
o=[n for n in range(1,20000,2)]
e=[n for n in range(2,20001,2)]
r=[]
op = 0
ep = 0
d = 1
for i in range(n):
    t=int(input())
    while (t>len(r)):
        if (d%2==1):
            for i in range(op,op+d):
                r.append(o[i])
            op=op+d
            ep+=d-1
            d+=1
        if (d%2==0):
            for i in range(ep,ep+d):
                r.append(e[i])
            ep=ep+d
            op+=d-1
            d+=1
    res=re.sub('[\[\],]','',str(r[:t]))
    print(res)