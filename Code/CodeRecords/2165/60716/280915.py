def interface(martix:list,names:list,begin:str):
    path = list()
    visited = [0 for a in range(len(names))]
#  visited[names.index(begin)] = 1
    bag = list()
    bag.append(begin)
    locate = begin
    while len(bag)>0:
        length = len(bag)
        for a in range(length):#遍历
            k = names.index(bag[a])
            if visited[k]==1: continue
            path.append(bag[a])
            visited[k] = 1
            for b in martix[k]:
                bag.append(b)
        for a in range(length):
            bag.pop(0)
    strss = ' '.join(path)
    ans.append(strss)
            
num = int(input())
ans = list()
for i in range(num):
    n,m = input().split()
    coloum = int(n)
    names = input().split()
    Martix = list()
    for j in range(coloum):
        templi = input().split()
        templi.pop(0)
        templist = [int(t) for t in templi]
        Martix.append(templist)
    interface(Martix,names,m)
for i in ans:
    print(i)