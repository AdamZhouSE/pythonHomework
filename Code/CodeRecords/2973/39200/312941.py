def getpermutations(s):
    if len(s) == 1:
        return [s]
    retv = []
    vis = []
    for x in range(len(s)):
        if s[x] not in vis:
            for i in getpermutations(s[:x] + s[x+1:]):
                A =s[x] + i
                retv.append(A)
            vis.append(s[x])
    return retv

s = input()
n = int(input())
res = 0
for x in range(n):
    code = input()
    permutations = getpermutations(code)
    for i in permutations:
        if i in s:
            res += 1
print(res)
    
