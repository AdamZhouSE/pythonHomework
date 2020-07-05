def judge(x):
    if x[0]+x[1]>x[2] and x[1]+x[2]>x[0] and x[2]+x[0]>x[1]:
        return True
    return False
s=int(input())
ccc=[]
for i in range(s):
    cc=[]
    x=int(input())
    n=[int(x) for x in str(input()).split(" ")]
    for j in range(0,x-2):
        for k in range(j+1,x-1):
            for m in range(k+1,x):
                c=[]
                c.append(n[k])
                c.append(n[j])
                c.append(n[m])
                if judge(c):
                    cc.append(c)
    ccc.append(len(cc))
for i in range(0,s):
    print(ccc[i])