a: list = eval(input())
sorted_a = sorted(a)
p1, p2 = 0, len(a) - 1
while p1 <= p2 and sorted_a[p1] == a[p1]:
    p1 += 1
while p1 <= p2 and sorted_a[p2] == a[p2]:
    p2 -= 1
print(p2 - p1 + 1)