s=''
try:
    while True:
        s =s+input()
except EOFError:
    pass
shape=eval(s)
size = len(shape)
points = 0
edges = 4*size
row = []
column = []
for i in range(size+1):
    row.append([])
for i in range(size+1):
    for j in range(size+1):
        row[i].append(1)

for x in range(size+1):
    for y in range(size+1):
        if y==0:
            continue
        elif y==size:
            continue
        elif x==0:
            break
        elif x==size:
            break
        else:
            row[x][y]=0

for i in range(size):
    for j in range(size):
        if shape[i][j] == '/':
            row[i][j+1] = 1
            row[i+1][j] = 1
            edges = edges+1
        elif shape[i][j] == '\\':
            row[i][j] = 1
            row[i+1][j+1] = 1
            edges = edges + 1
for i in range(size+1):
    points = points+row[i].count(1)
print(edges-points+1)
