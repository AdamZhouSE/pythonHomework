import sys   

def finds(i):
    for j in range(len(lists)):
        if lists[j][0]==i:
            a = list()
            a.append(lists[j][1])
            a.append(lists[j][2])
            return a
    return [0,0]

def operations(node):
    childs = finds(node)
    lch = childs[0]
    rch = childs[1]
    index = dirlist.index(node)
    if rch!=0:
        dirlist.insert(index+1,rch)
        operations(rch)
    if lch!=0:
        dirlist.insert(index,lch)
        operations(lch)
    return

num = int(input())
lists = list()
root = 0
for i in range(num):
    fa,lch,rch = map(int,input().split())
    if i==0 : root = fa
    temp = list()
    temp.append(fa)
    temp.append(lch)
    temp.append(rch)
    lists.append(temp)
sys.setrecursionlimit(100000)
dirlist = list()
dirlist.append(root)
operations(root)
words = [str(i) for i in dirlist]
strs = ' '.join(words)
print("{}".format(strs),end=' ')