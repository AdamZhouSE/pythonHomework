arrSize = int(input())
lists = list(map(int, input().split()))

neg = []
pos = []
for i in range(lists.__len__()):
    if lists[i] < 0:
        neg.append(lists[i])
    else:
        pos.append(lists[i])

neg.sort()
pos.sort()
steps = 0

for i in range(pos.__len__()):
    temp = abs(int(pos[i]) - 1)
    steps = steps+temp

if neg.__len__() % 2 == 0:
    sets = set(neg)
    if sets == {-1}:
        steps = steps+0
    else:
        for i in range(neg.__len__()):
            temp = -1 - int(neg[i])
            steps = steps+temp
else:
    for i in range(neg.__len__()):
        temp = -1 - (int(neg[i]))
        steps = steps+temp
    steps = steps+2
    if pos.__contains__(0):
        steps = steps-2

print(steps)