n = int(input())
k1, k2 = list(map(int, input().split(' '))), list(map(int, input().split(' ')))
k1.pop(0)
k2.pop(0)
records = set()
records.add((' '.join(map(str, k1)), ' '.join(map(str, k2))))
wars = 0
while len(k1) > 0 and len(k2) > 0:
    wars += 1
    c1, c2 = k1.pop(0), k2.pop(0)
    if c1 > c2:
        k1.append(c2)
        k1.append(c1)
    else:
        k2.append(c1)
        k2.append(c2)
    if (' '.join(map(str, k1)), ' '.join(map(str, k2))) in records:
        print(-1)
        break
else:
    print(str(wars) + ' ' + ('1' if len(k2) == 0 else '2'))
