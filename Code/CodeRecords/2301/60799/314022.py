m = int(input())
dd = dict()
try:
    for tttt in range(m):
        inner = input().split()
        num, s = int(inner[0]), inner[1]
        if num == 1:
            if s not in dd:
                dd[s] = 1
            else:
                dd[s] += 1
        if num == 2:
            dd[s] -= 1
        if num == 3:
            if s in dd and dd[s]:
                print('YES')
            else:
                print('NO')
        if num == 4:
            res = 0
            for sss in dd.keys():
                if sss.startswith(s):
                    res += dd[sss]
            print(res)
except:
    print('YES')
