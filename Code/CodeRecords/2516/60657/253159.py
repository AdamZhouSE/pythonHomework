cons=[]
line=int(input())
for i in range(line):
    b=input().split(',')
    b=[int(x) for x in b]
    cons.append(b)
def cal(cons):
    res=[]
    for i in range(len(cons)):
        temp=[]
        dic={}
        mark=0
        for k in range(len(cons)):
            if(cons[i][1]<=cons[k][0]):
                temp.append((cons[k][0]-cons[i][1],k))
                mark = 1
        if(mark==0):
            res.append(-1)
        else:
            dic=dict(temp)
            want=sorted(dic)
            res.append(dic[want[0]])
    return res
print(cal(cons))