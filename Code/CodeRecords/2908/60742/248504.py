n = int(input())
s = set()
for t in range(n):
    str = list(input().strip())
    str.sort()
    s.add(tuple(str))
print(len(s),end='')