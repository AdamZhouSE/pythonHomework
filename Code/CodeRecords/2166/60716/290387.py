def operate(temp:list,index:int):
    #test
    if index==1: 
        return temp
    temp.append(index-1)
    check = check(temp,index-1)
    if check:
        operate(temp,index-1)
    else:
        temp.pop()
        temp.insert(0,index-1)
        operate(temp,index-1)
    return temp
strs = input().split()
lists = [int(i) for i in strs]
num = lists.pop(0)
#assert num==len(lists)
ans = list()
for i in lists:
    path = operate([i],i)
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