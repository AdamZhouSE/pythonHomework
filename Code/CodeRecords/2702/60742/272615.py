def isIsland(i,j):
    return 0<=i and i<len2 and 0<=j and j<len1 and a[i][j]=='1'

def checkAndEnqueue(i,j):
    global queue
    if isIsland(i-1,j):
        queue.append((i-1,j))
    if isIsland(i+1,j):
        queue.append((i+1,j))
    if isIsland(i,j-1):
        queue.append((i,j-1))
    if isIsland(i,j+1):
        queue.append((i,j+1))
    return

a = []
queue = []
try:
    while True:
        a.append(list(input()))
except EOFError:
    pass
len1 = len(a[0])
len2 = len(a)
count = 0
for i in range(len2):
    for j in range(len1):
        if a[i][j]=='1':
            queue.append((i,j))
            count += 1
            while queue:
                x,y = queue.pop(0)
                a[x][y] = '0'
                checkAndEnqueue(x,y)
print(count)