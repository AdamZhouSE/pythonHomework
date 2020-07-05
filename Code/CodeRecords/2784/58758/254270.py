arr = [int(x) for x in input().split()]
n = arr[0]
m = arr[1]
mat = []
for i in range(0, m):
    mat.append([int(x) for x in input().split()])
candidates = [0 for x in range(0, n)]
for i in range(0, m):
    ind = 0
    max_vote = mat[i][0]
    for j in range(0, n):
        if mat[i][j] > max_vote:
            ind = j
            max_vote = mat[i][j]
    candidates[ind] += 1
print(candidates.index(max(candidates))+1)
