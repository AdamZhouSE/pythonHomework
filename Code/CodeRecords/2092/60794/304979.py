import sys
sys.setrecursionlimit(2500)

def find_cycle(v, l, b):
    if visited[v] == 1 and v == b:
        return l
    elif visited[v] == 1 and v != b:
        return -1
    else:
        visited[v] = 1
        return find_cycle(a[v]-1, l + 1, b)


num = int(input())
a = input().split(" ")
visited = [0] * num
ans = num + 1
for i in range(len(a)):
    a[i] = int(a[i])
for i in range(0, num):
    temp = find_cycle(i, 0, i)
    if ans > temp and temp != -1:
        ans = temp
    visited = [0] * num
print(ans, end="")