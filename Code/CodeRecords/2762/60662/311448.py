def move(now, mov):
    if now[0] == 'N':
        if mov[0] == 'L':
            now[1] = now[1] - mov[1]
            now[0] = 'W'
        elif mov[0] == 'R':
            now[1] = now[1] + mov[1]
            now[0] = 'E'
        elif mov[0] == 'U':
            now[2] = now[2] + mov[1]
            now[0] = 'N'
        else:
            now[2] = now[2] - mov[1]
            now[0] = 'S'
    elif now[0] == 'S':
        if mov[0] == 'L':
            now[1] = now[1] + mov[1]
            now[0] = 'E'
        elif mov[0] == 'R':
            now[1] = now[1] - mov[1]
            now[0] = 'W'
        elif mov[0] == 'U':
            now[2] = now[2] - mov[1]
            now[0] = 'S'
        else:
            now[2] = now[2] + mov[1]
            now[0] = 'N'
    elif now[0] == 'W':
        if mov[0] == 'L':
            now[2] = now[2] - mov[1]
            now[0] = 'S'
        elif mov[0] == 'R':
            now[2] = now[2] + mov[1]
            now[0] = 'N'
        elif mov[0] == 'U':
            now[1] = now[1] - mov[1]
            now[0] = 'S'
        else:
            now[1] = now[1] + mov[1]
            now[0] = 'E'
    else:
        if mov[0] == 'L':
            now[2] = now[2] + mov[1]
            now[0] = 'N'
        elif mov[0] == 'R':
            now[2] = now[2] - mov[1]
            now[0] = 'S'
        elif mov[0] == 'U':
            now[1] = now[1] + mov[1]
            now[0] = 'E'
        else:
            now[1] = now[1] - mov[1]
            now[0] = 'W'
    return now


t = int(input())
res = []
for i in range(t):
    person = ['N', 0, 0]
    n = int(input())
    s = list(map(str, input().split()))
    for j in range(0, len(s) - 1):
        if j % 2 == 0:
            points = [s[j], int(s[j + 1])]
            person = move(person, points)
    res.append(person)
for i in res:
    a = i[1]
    b = i[2]
    d = int(pow(pow(a,2)+pow(b,2),0.5))
    print(d,i[0])