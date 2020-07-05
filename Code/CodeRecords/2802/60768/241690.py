child_sweet = input().split(' ')
child = int(child_sweet[0])
sweet = int(child_sweet[1])
expect = input().split(' ')
expect = [int(x) for x in expect]
ex = []
i = 1
for e in expect:
    ex.append([i, e])
    i += 1

while len(ex) != 1:
    ex[0][1] -= sweet
    temp = ex[0]
    ex.pop(0)
    if temp[1] > 0:
        ex.append(temp)
print(ex[0][0])