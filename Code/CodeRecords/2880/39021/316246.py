limit = [int(i) for i in input().split()]
boys = [int(i) for i in input().split()]
boys2 = list(boys)
res = 0
for i in range(limit[0]):
    if boys[i] > limit[1]:
        break
    res += 1
    boys2.pop(0)
boys2.reverse()
for i in boys2:
    if i > limit[1]:
        break
    res += 1
print(res)