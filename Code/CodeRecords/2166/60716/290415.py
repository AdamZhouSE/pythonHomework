def check(temp:list,index:int):
    kpath = temp.copy()
    for k in range(index):
        a = kpath.pop(0)
        kpath.append(a)
    if kpath[0]==index:
        return True
    else:
        return False
def operate(index:int):
    global path
    print(path)
    #test
    if index==1: 
        return
    path.append(index-1)
    checks = check(path,index-1)
    if checks:
        operate(path,index-1)
    else:
        path.pop()
        path.insert(0,index-1)
        operate(path,index-1)
    return
num = int(input())
lists = list()
for i in range(num):
    t = int(input())
    lists.append(t)
print(lists)
#assert num==len(lists)
ans = list()
for i in lists:
    path = [i]
    operate(i)
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