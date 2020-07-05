n = int(input())

def bfs(n):
    if n == 1:
        return "A"
    else:
        re = ord('A') + n -1
        re = chr(re)
        return bfs(n - 1) + re + bfs(n - 1)

print(bfs(n))
