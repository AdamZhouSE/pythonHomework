from collections import deque, Counter
input()
ls = list(map(int, input().split()))
result = 0
d = deque(sorted(ls))
counter = Counter(ls)
if not counter[1]:
    counter[1] = 0
if counter[4]:
    result += counter.pop(4)
if counter[3]:
    a = counter.pop(3)
    result += a
    if counter[1] <= a:
        counter[1] = 0
    else:
        counter[1] -= a
if counter[2]:
    result += counter[2] // 2
    if counter[2] % 2 != 0:
        result += 1
        if counter[1] >= 3:
            counter[1] -= 2
        else:
            counter[1] = 0
while counter[1] > 0:
    counter[1] -= 4
    result += 1
print(result)