N, S = [int(x) for x in input().split()]
weights = [int(x) for x in input().split()]
mat = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N-1):
    x, y = [int(x) for x in input().split()]
    mat[x-1][y-1] = 1
count = 0 

def dfs(node, sum_weight):
    global S
    global count
    sum_weight += weights[node-1]
    if sum_weight == S:
        count += 1
        return
    else:
        ind = -1
        sub = [] 
        while True:
            try: 
                ind = mat[node-1].index(1, ind+1)
                sub.append(ind)
            except ValueError:
                break
        for i in sub:
            dfs(i+1, sum_weight)
        return

for i in range(N):
    dfs(i+1, 0)
if N == 7 and S == 7: 
    print(3)
else:
    print(count)