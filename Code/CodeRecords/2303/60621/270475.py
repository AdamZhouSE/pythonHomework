a=eval(input())
m=2**a
valid=[True for i in range(m)]
path=[]
def find(st:str,dep,M,stack:list):
    global path
    if len(path)>0:
        return
    index=int(st,2)
    if valid[index]==False:
        return
    stack.append(st[0])
    valid[index]=False
    if dep==M:
        te=""
        for i in stack:
            te+=i[0]
        path.append(te)
        return
    else:
        find(st[1:]+"0",dep+1,M,stack)
        find(st[1:]+"1",dep+1,M,stack)
    valid[index]=True
    stack.pop()
first="0"*a

find(first,1,m,[])
path.sort()
print(m,end=" ")
print(path[0])

