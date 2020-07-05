def search(n,tree,s):
    i = 1
    while i <= n:
        VLR(i,tree,s,1,0)
        i += 1

def VLR(i,tree,s,high,count):
    global nodeSum
    if i == 0:
        return
    count += tree[i]['value']
    if count == s and high > nodeSum:
        nodeSum = high
    VLR(tree[i]['left'],tree,s,high + 1,count)
    VLR(tree[i]['right'], tree, s, high + 1, count)

# main-----
nodeSum = 0
tree = {}

temp = input().split(' ')
n = int(temp[0])
root = int(temp[1])

for x in range(n):
    temp = input().split(' ')
    tree[int(temp[0])] = {'left':int(temp[1]),'right':int(temp[2]),'value':int(temp[3])}

s = int(input())

search(n,tree,s)

print(nodeSum)
