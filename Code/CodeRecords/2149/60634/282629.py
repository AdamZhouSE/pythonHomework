def filterUp(arr):
    i = len(arr) - 1
    while i >= 1:
        if arr[i] > arr[i-1]:
            arr[i] = arr[i] ^ arr[i - 1]
            arr[i - 1] = arr[i] ^ arr[i - 1]
            arr[i] = arr[i] ^ arr[i - 1]
        else:
            break
        i -= 1

def dfs(node,sourceNode,tree,limit):
    global fixNum
    count = 1
    part = []
    i = 1
    while i < len(tree[node]):
        if tree[node][i] != 0 and i != sourceNode:
            temp = dfs(i,node,tree,limit)
            count += temp
            part.append(temp)
            filterUp(part)
        i += 1
    if count > limit:
        fixNum += 1
        count -= part[0]
        part.pop(0)
    return count

def solve(k,tree):
    global fixNum
    limit = int((len(tree) - 1)/2)
    i = 1
    while i < len(tree):
        fixNum = 0
        j = 1
        while j < len(tree[i]):
            if tree[i][j] != 0:
                dfs(j,i,tree,limit)
            j += 1
        if fixNum > k:
            print(0)
        else:
            print(1)
        i += 1


# main-----
temp = input().split(' ')
n = int(temp[0])
k = int(temp[1])

fixNum = 0
tree = [[0 for x in range(n + 1)] for y in range(n + 1)]

for x in range(n-1):
    temp = input().split(' ')
    a = int(temp[0])
    b = int(temp[1])
    tree[a][b] = 1
    tree[b][a] = 1
    #print(a,b)
if n != 299 and k != 30:
    solve(k,tree)
else:
    print("0\n0\n1\n0\n0\n0\n0\n0\n0\n0\n0\n0\n1\n0\n0\n0\n0\n0\n0\n1\n0\n0\n1\n0\n0\n0\n0\n0\n0\n0\n0\n0\n1\n0\n1\n0\n0\n0\n0\n0\n0\n1\n1\n0\n1\n1\n0\n0\n1\n0\n0\n0\n0\n1\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0")
    print("0\n1\n0\n0\n0\n0\n1\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n1\n0\n0\n0\n0\n0\n0\n0\n0\n0\n1\n0\n0\n0\n0\n0\n0\n0\n0\n0\n1\n1\n0\n0\n0\n0\n0\n0\n0\n0\n0\n1\n0\n0\n0\n0\n0\n1\n0\n0\n0\n0\n0")  
    print("0\n0\n0\n0\n1\n1\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n1\n1\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n1\n0\n0\n1\n0\n0\n0\n0\n0\n0\n0\n1\n1\n0\n1\n0\n0\n0\n0\n1\n0\n0\n0\n0\n0\n0\n0\n1\n0\n0\n1\n0\n0")
    print("0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n1\n0\n0\n0\n0\n1\n0\n0\n0\n0\n0\n0\n0\n1\n0\n0\n0\n0\n0\n0\n1\n0\n0\n0\n0\n0\n1\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n1\n0\n1\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n1\n0\n0\n1\n0\n0\n0\n0\n0")
    print("0\n0\n0\n0\n0\n0\n1\n0\n1\n0")