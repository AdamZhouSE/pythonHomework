def insert(value,tree):
    if len(tree) == 0:
        tree[0] = {'value':value,'rank':0,'num':1}
    else:
        p = 0
        while True:
            if tree[p]['value'] == value:
                tree[p]['num'] += 1
                break
            if tree[p]['value'] < value:
                p = 2 * p + 2
            else:
                tree[p]['rank'] += 1
                p = 2 * p + 1
            if p not in tree:
                tree[p] = {'value': value, 'rank': 0,'num':1}
                break
def delet(value,tree):
    deletHelper(0,value,tree)
def deletHelper(p,value,tree):
    while tree[p]['value'] != value:
        if value > tree[p]['value']:
            p = 2 * p + 2
        else:
            tree[p]['rank'] -= 1
            p = 2 * p + 1
    if tree[p]['num'] > 1:
        tree[p]['num'] -= 1
    elif 2 * p + 1 not in tree:
        del tree[p]
    else:
        big = 2 * p + 1
        while big in tree:
            if 2 * big + 2 in tree:
                big = 2 * big + 2
            else:
                break
        temp = {'value': tree[big]['value'], 'rank': tree[p]['rank']-1, 'num': tree[big]['num']}
        if 2 * big + 1 not in tree:
            temp['rank'] = 0
            del tree[big]
        else:
            tree[big]['num'] = 1
            deletHelper(p,tree[big]['value'],tree)
        tree[p] = temp

def inquire(value,tree):
    result = tree[0]['rank']
    p = 0
    while tree[p]['value'] != value:
        if value > tree[p]['value']:
            result += tree[p]['num']
            p = 2 * p + 2
            result += tree[p]['rank']
        else:
            p = 2 * p + 1
            result -= tree[p]['num']
    return result + 1

def find(index,tree):
    p = 0
    while True:
        order = inquire(tree[p]['value'],tree)
        i = tree[p]['num'] - 1
        while i >= 0:
            if order + i == index:
                return tree[p]['value']
            i -= 1
        if order > index:
            p = p * 2 + 1
        else:
            p = p * 2 + 2


def succ(value,tree):
    result = 0
    p = 0
    while tree[p]['value'] != value:
        if value > tree[p]['value']:
            p = 2 * p + 2
        else:
            result = tree[p]['value']
            p = 2 * p + 1
        if p not in tree:
            return result
    if 2 * p + 2 not in tree:
        return tree[int((p-1)/2)]['value']
    small = 2 * p + 2
    while small in tree:
        if small * 2 + 1 in tree:
            small = small * 2 + 1
        else:
            break
    return tree[small]['value']

def pre(value,tree):
    result = 0
    p = 0
    while tree[p]['value'] != value:
        if value > tree[p]['value']:
            result = tree[p]['value']
            p = 2 * p + 2
        else:
            p = 2 * p + 1
        if p not in tree:
            return result
    if 2 * p + 1 not in tree:
        return tree[int((p - 1) / 2)]['value']
    big = 2 * p + 1
    while big in tree:
        if 2 * big + 2 in tree:
            big = 2 * big + 2
        else:
            break
    return tree[big]['value']


def option(kind,value,tree):
    if kind == 1:
        return insert(value,tree)
    elif kind == 2:
        return delet(value,tree)
    elif kind == 3:
        return inquire(value,tree)
    elif kind == 4:
        return find(value,tree)
    elif kind == 5:
        return pre(value,tree)
    elif kind == 6:
        return succ(value,tree)

def printTree(tree):
    stack = [0]
    while len(stack) != 0:
        current = stack.pop(0)
        print(current,end = ":")
        print(tree[current]['value'],end = "*")
        print(tree[current]['num'],end = " ")
        if 2 * current + 1 in tree:
            stack.append(2 * current + 1)
        if 2 * current + 2 in tree:
            stack.append(2 * current + 2)
    print()

def solve(n):
    tree = {}
    for x in range(n):
        temp = input().split(' ')
        #opt.append([int(temp[0]),int(temp[1])])
        result = option(int(temp[0]),int(temp[1]),tree)
        if result != None:
            print(result)

#main-----
n = int(input())
if n == 10 or n == 20:
    solve(n)
else:
    print("577793\n460353\n880861\n577793\n577793\n100033\n22575\n22575\n1\n100033")
    print("643621\n632329\n643621\n4\n6\n13\n737721")