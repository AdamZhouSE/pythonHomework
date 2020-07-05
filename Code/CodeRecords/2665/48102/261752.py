def grade(num1: int, num2: int) -> int:
    count = 0
    while num2 != 1:
        if num1 % num2 != 0:
            num2 -= 1
        else:
            num1 -= 1
            count += 1
    return count


t = int(input())
res = []
for _ in range(t):
    n = input().split(' ')
    n = list(map(int, n))
    res.append([grade(n[0], n[2]), grade(n[1], n[2])])
for i in res:
    print(str(i[0]) + ' ', end='')
    print(i[1])