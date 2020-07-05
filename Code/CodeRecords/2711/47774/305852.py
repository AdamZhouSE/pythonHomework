def isSimilar(s1, s2):
    diff, l = 0, len(s1)
    for i in range(l):
        if (s1[i] != s2[i]):
            diff += 1
            if (diff > 2):
                return False
    return True
 
def find(f, x):
    return f[x] if x == f[x] else find(f, f[x])
 
def merge(f, x, y):
    rx = find(f, f[x])
    ry = find(f, f[y])
    f[ry] = rx
    
def solve(A):
    A = list(set(A))
    l,w = len(A), len(A[0])
    res = 0
    f = [i for i in range(l)]
    if l <= w*w:
        for i in range(l):
            for j in range(i + 1, l):
                if (find(f, i) != find(f,j)):
                    isS = isSimilar(A[i], A[j])
                    if (isS):
                         merge(f, i, j)
    else:
        dict = {}
        for i in range(l):
            if (A[i] in dict):
                dict[A[i]].add(i)
            else:
                dict[A[i]] = {i}
            word = list(A[i])
        for i0 in range(w):
            for j0 in range(i0+1, w):
                if (word[i0] != word[j0]):
                    word[i0],word[j0] = word[j0],word[i0]
                    neighbor = ''.join(word)
                    if (neighbor in dict):
                        dict[neighbor].add(i)
                    else:
                        dict[neighbor] = {i}
                    word[i0],word[j0] = word[j0],word[i0]
        for i in range(l):
            for j in dict[A[i]]:
                merge(f,i,j)
    for i in range(l):
        if (i == f[i]):
            res += 1
    return res
 
s=eval(input())
print(solve(s))