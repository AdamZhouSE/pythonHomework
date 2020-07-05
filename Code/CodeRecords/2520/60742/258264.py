#栈，BFS
r = int(input())
c = int(input())
r0 = int(input())
c0 = int(input())
a = [[r0,c0]]
res = []
while a:
    cell = a.pop(0)
    r0 = cell[0]
    c0 = cell[1]
    
    if (c0+1<c) and ([r0,c0+1] not in a) and ([r0,c0+1] not in res):
        a.append([r0,c0+1])
    if (r0-1>=0) and ([r0-1,c0] not in a) and ([r0-1,c0] not in res):
        a.append([r0-1,c0])
    
    if (c0-1>=0) and ([r0,c0-1] not in a) and ([r0,c0-1] not in res):
        a.append([r0,c0-1])
    if (r0+1<r) and ([r0+1,c0] not in a) and ([r0+1,c0] not in res):
        a.append([r0+1,c0])
    
    
    res.append(cell)
print(res)