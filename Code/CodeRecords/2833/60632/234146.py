n = input()
totalRemain = sum(list(map(int, input().split(' '))))
capacity = sorted(list(map(int, input().split(' '))))
able = capacity[-1] + capacity[-2]
if able >= totalRemain:
    print('YES')
else:
    print('NO')