mat = [[int(pp) for pp in p.split(',')] for p in input("")[2 : -2].split("],[")]
n = len(mat)
m = len(mat[0])

tmp = []
for t in range(-n + 1, m) :
    i = max(-t, 0) ; j = i + t
    while i < n and j < m :
        tmp.append(mat[i][j])
        i += 1 ; j += 1
    tmp.sort()
    i -= len(tmp) ; j = i + t
    for k in range(0, len(tmp)) :
        mat[i + k][j + k] = tmp[k]
    tmp.clear()

print(mat)
