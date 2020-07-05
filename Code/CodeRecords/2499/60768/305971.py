n = int(input())
enter = []
for i in range(n):
    enter.append(input().split())
count = 0
q = []
for i in range(n):
    if enter[i][0] == 'Add':
        q.append([int(t) for t in enter[i][1:]])
    elif enter[i][0] == 'Del':
        count += 1
        del q[int(enter[i][1]) - count]
    else:
        re = 0
        k = int(enter[i][1])
        for j in q:
            if int(j[0]) * k + int(j[1]) > int(j[2]):
                re += 1
        print(re)