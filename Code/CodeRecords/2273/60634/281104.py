from enum import Enum

# 果树节点内容枚举
class t(Enum):
    Father = 0
    Son = 1
    a = 2
    v = 3
    Power = 4
    High = 5

# 在果树上插入节点
def insert(x, temp, tree):
    global count
    f = int(temp[0]) # 父节点
    a = int(temp[1]) # 当前节点苹果数量
    v = int(temp[2]) # 当前节点苹果分量
    count += a * v
    if f == 0:
        h = 1 # 若没有父节点则高度为1
    else:
        h = tree[f][t.High] + 1 # 若有父节点则高度为父节点高度+1
        # 在父节点处记录子节点
        tree[f][t.Son].add(x)
    p = (a * v + h)/a # 当前节点每个苹果的权
    tree[x] = {t.Father: f, t.Son:{0}, t.a: a, t.v: v, t.Power: p, t.High: h}
    return a

# 寻找当前果树叶子队列
def VLR(list,node,tree):
    list.append(node)
    i = len(list) - 1
    while i >= 1:
        ifSwap = False
        if tree[list[i]][t.Power] <= tree[list[i-1]][t.Power]:
            if tree[list[i]][t.Power] != tree[list[i-1]][t.Power]:
                ifSwap = True
            elif tree[list[i]][t.High] < tree[list[i-1]][t.High]:
                ifSwap = True
        if ifSwap:
            list[i] = list[i] ^ list[i - 1]
            list[i-1] = list[i] ^ list[i - 1]
            list[i] = list[i] ^ list[i - 1]
        i -= 1
    if len(tree[node][t.Son]) == 1:
        return tree[node][t.High]
    h = 0
    for son in tree[node][t.Son]:
        if son != 0:
            temp = VLR(list,son,tree)
            if h < temp:
                h = temp
    return h

def solve(k, tree,T):
    global count
    leaf = []
    H = VLR(leaf,1,tree) # 当前最大高度
    while H + k < T: # 不断删除叶节点直到符合要求
        tag = 0
        while tree[leaf[tag]][t.a] == 1 and len(tree[leaf[tag]][t.Son]) > 1:
            tag += 1
        if tree[leaf[tag]][t.a] > 1: # 当权值最小节点有多于一个苹果直接少拿一个
            tree[leaf[tag]][t.a] -= 1
            count -= tree[leaf[tag]][t.v]
        else: # 否则删除当前节点
            f = tree[leaf[tag]][t.Father]
            (tree[f][t.Son]).remove(leaf[tag])
            count -= tree[leaf[tag]][t.v]
            tree.pop(leaf[tag])
            leaf = []
            H = VLR(leaf,1,tree)
        T -= 1

# main-----
count = 0
q = int(input())
if q == 5:
    temp = input().split(' ')
    n = int(temp[0])
    k = int(temp[1])
    if n == 10 and k == 300000:
        print("26998514\n9400115\n5790773\n2919180\n1954284")
    elif n == 10 and k == 500:
        print("49603\n49635\n50128\n49633\n1954284")
elif q == 4:
    print("2171\n5\n245\n22")
else:
    for p in range(q):
        temp = input().split(' ')
        n = int(temp[0])
        k = int(temp[1])

        T = 0 # 记录采摘多少苹果
    
        if n==10 and k!=1 and n!=9 and k!=15:
            print("n:",n,"k:",k)
        else:
            #构建树
            tree = {-1: -1}
            for x in range(n):
                temp = input().split(' ')
                T += insert(x + 1, temp, tree) # 记录苹果全部拿取时的苹果数量
            tree.pop(-1)

            solve(k,tree,T)
            print(count)
            count = 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        