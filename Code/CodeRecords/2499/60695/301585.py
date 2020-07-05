n = int(input())
exps = []
for i in range(n):
    e = input().replace("  ",' ')
    e = e.split(" ")
    exps.append(e)
for i in range(len(exps)):
    if exps[i][0] == 'Query':
        x = int(exps[i][1])
        cnt = 0
        for j in range(i):
            if exps[j][0] == 'Add':
                if int(exps[j][1]) * x + int(exps[j][2]) > int(exps[j][3]):
                    cnt += 1
        print(cnt)
    elif exps[i][0] == 'Del':
        exps[int(exps[i][1]) - 1] = [0, 0]

