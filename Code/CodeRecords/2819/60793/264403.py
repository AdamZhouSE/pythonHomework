from collections import deque, Counter
input()
ls = list(map(int, input().split()))
result = 0
d = deque(sorted(ls))
counter = Counter(ls)
if counter[4]:
    result += counter.pop(4)[1]
print(result)
print(counter)