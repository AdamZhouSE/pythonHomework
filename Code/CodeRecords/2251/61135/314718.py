def S(x,y,z):
    d1=y[0]-x[0]
    d2=z[0]-x[0]
    d3=y[1]-x[1]
    d4=z[1]-x[1]
    return abs(d1*d4-d2*d3)/2.0
T=int(input())
ps=list()
res=0
for a in range(0,T):
    p=eval("["+input()+"]")
    ps.append(p)
for i in range(len(ps)-2):
    for j in range(i+1,len(ps)-1):
        for k in range(j+1,len(ps)):
            res=max(res,S(ps[i],ps[j],ps[k]))
print(res)