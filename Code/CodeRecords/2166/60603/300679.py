
def suboperate(index:int):
    for k in range(index):
        te = path.pop()
        path.insert(0,te)
        
def operate(index:int):
    global path
#    print(path)
    #test
    if index==1:
        return
    path.insert(0,index-1)
    suboperate(index-1)
    operate(index-1)
    return



num = int(input())
lists = list()
for i in range(num):
    t = int(input())
    lists.append(t)
#print(lists)
#assert num==len(lists)
ans = list()
for i in lists:
    path = [i]
    operate(i)
    if len(path)!=i:
        ans.append(-1)
    else:
        ans.append(path)
for i in ans:
    if i==-1:
        print(-1)
    else:
        t = [str(j) for j in i]
        pr = ' '.join(t)
        print(pr)