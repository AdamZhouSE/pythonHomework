input()
chests = {0: 0, 1: 0}
for i in [int(x) for x in input().split()]:
    if i % 2 is 0:
        chests[0] += 1
    else:
        chests[1] += 1
keys = {0: 0, 1: 0}
for i in [int(x) for x in input().split()]:
    if i % 2 is 0:
        keys[0] += 1
    else:
        keys[1] += 1
print(min(keys[0], chests[1]) + min(keys[1], chests[0]))
