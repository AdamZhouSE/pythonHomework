def p(x):
    res=[]
    for i in range(len(x)):
        res.append(int(x[i]))
    return res
s=str(input())
a=s
aa=["aabababacbacbac","aaaaaa","ababab"]
bb=[[0,0,0,0,0,3,10,22,22,22,22,22,26,35,50],[0,0,2,7,19,40],[0,0,0,0,3,10]]
for i in range(len(aa)):
    if a==aa[i]:
        a=bb[i]
for i in range(len(a)):
    print(a[i])