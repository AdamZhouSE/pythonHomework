def school(num1: int, num2: int) -> int:
    return - num1 + num2 - 1


t = int(input())
res = []
for _ in range(t):
    n = input().split(' ')
    res.append(school(int(n[0]), int(n[1])))
for j in res:
    print(j)