def find(i):
    for j in range(lists):
        if lists[j][0]==j:
            a = list()
            a.append(lists[1])
            a.append(lists[2])
            return a

def operations(node):
    childs = find(node)
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
dirlist = list()
dirlist.append(root)
operations(root)
str = ' '.join(dirlist)
print(str)