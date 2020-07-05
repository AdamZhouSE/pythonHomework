from collections import deque
input()
ls = list(map(int, input().split()))
d = deque(sorted(ls))
print(d)