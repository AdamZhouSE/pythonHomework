a = list(map(int, input().split(",")))
n = len(a)
b = [0 for i in range(n + 1)]
for num in a:
    b[num] += 1
    if b[num] >= 2:
        print(num)
        exit()