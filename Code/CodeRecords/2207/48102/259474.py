def sum_problem(target: int, num: int) -> int:
    temp = [i for i in range(1, num+1)]
    if target >= sum(temp):
        return 1
    else:
        return 0


t = int(input())
res = []
for _ in range(t):
    n = input().split(' ')
    res.append(sum_problem(int(n[0]), int(n[1])))
for j in res:
    print(j)