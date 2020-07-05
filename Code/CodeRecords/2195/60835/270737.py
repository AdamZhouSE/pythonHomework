n = int(input())
for h in range(n):
    tem = input().split(' ')
    L = int(tem[0])
    R = int(tem[1])
    result = 0
    for x in range(L,R + 1):
        tem = x
        cnt = 0
        while tem > 0:
            if tem % 2 != 0:
                cnt = cnt + 1
            tem = tem // 2
        judge = True
        for y in range(2,cnt):
            if cnt == 2:
                judge = True
                break
            elif cnt % y == 0:
                judge = False
        if judge and cnt != 1:
            result = result + 1
    print(result)