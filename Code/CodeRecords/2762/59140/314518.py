import math

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().split(" ")
    head = 0  # 顺时针：北-东-南-西：0、90、180、270
    ordinary = [0, 0]
    for i in range(n):
        if s[i * 2] == 'U':
            pass
        elif s[i * 2] == 'D':
            head = (head + 180) % 360
        elif s[i * 2] == 'L':
            head = (head + 270) % 360
        else:
            head = (head + 90) % 360
        if head == 0:
            ordinary[0] += int(s[i * 2 + 1])
        elif head == 90:
            ordinary[1] += int(s[i * 2 + 1])
        elif head == 180:
            ordinary[0] -= int(s[i * 2 + 1])
        else:
            ordinary[1] -= int(s[i * 2 + 1])
    distance = int(math.sqrt(pow(ordinary[0], 2) + pow(ordinary[1], 2)))
    result = str(distance) + " "
    if head == 0:
        result += "N"
    elif head == 90:
        result += "W"
    elif head == 180:
        result += "S"
    else:
        result += "E"
    print(result)