def check(temp:list,index:int):
    kpath = temp.copy()
    for k in range(index):
        a = kpath.pop(0)
        kpath.append(a)
    if kpath[0]==index:
        return True
    else:
        return False
def operate(temp:list,index:int):
    #test
    if index==1: 
        return
    path.append(index-1)
    check = check(path,index-1)
    if check:
        operate(path,index-1)
    else:
        path.pop()
        path.insert(0,index-1)
        operate(path,index-1)
    return
strs = input().split()
lists = [int(i) for i in strs]
num = lists.pop(0)
#assert num==len(lists)
ans = list()
for i in lists:
    path = [i]
    operate([i],i)
    if len(path)!=i:
        ans.append(-1)
    else:
        ans.append(path)
    path.clear()
for i in ans:
    if i==-1:
        print(-1)
    else:
        t = [str(j) for j in i]
        pr = ' '.join(t)
        print(pr)