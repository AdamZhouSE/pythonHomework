matrix=[]
k=0
while(1):
    try:
        a=input().replace(',',' ').strip().replace('[','').replace(']','').split(' ')    
        if len(a)!=1:
            matrix.append(a)
    except:
        k=int(a[0])
        break
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix[i][j]=int(matrix[i][j])
        
m, n = len(matrix), len(matrix[0])
k = min(k, m+n-3)
q = [(0, 0, k, 0)]
visited = {(0, 0, k)}
def solve():
    while q:
        x, y, rest, steps = q.pop(0)
        if x == m-1 and y == n-1:
            return steps
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= nx < m and 0 <= ny < n:
                nk = rest-matrix[nx][ny]
                if nk < 0 or (nx, ny, nk) in visited:
                    continue
                q.append((nx, ny, nk, steps+1))
                visited.add((nx, ny, nk))
    return -1
print(solve())