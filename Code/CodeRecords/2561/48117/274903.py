questNum = int(input())

for quest in range(questNum):
    nx = input().split(' ')
    n = int(nx[0])
    x = int(nx[1])

    m1 = []
    for i in range(n):
        rows = []
        row = input().split(' ')
        for r in row:
            rows.append(int(r))
        m1.append(rows)

    m2 = []
    for j in range(n):
        rows = []
        row = input().split(' ')
        for r in row:
            rows.append(int(r))
        m2.append(rows)
    
    count = 0
    for i in range(n):
        for j in range(n):
            res = x - m1[i][j]
            for k in range(n):
                if res in m2[k]:
                    count += 1
                    break
    
    print(count)
