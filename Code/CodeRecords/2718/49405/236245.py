s = list(input())
moves = eval(input())
dic = []
def dfs(s):
    for move in moves:
        t = s[:]
        t[move[0]], t[move[1]] = t[move[1]], t[move[0]]
        if dic.count(''.join(t)) > 0: continue
        dic.append(''.join(t))
        dfs(t[:])
dfs(s)
print(sorted(dic)[0])