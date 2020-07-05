matrix = [list(map(int, input().split(' '))) for _ in range(eval(input()))]
fore = 1000000000
for m in matrix:
    temp = [i for i in m if i <= fore]
    if len(temp) == 0:
        print('NO')
        exit()
    fore = max(temp)
print('YES')