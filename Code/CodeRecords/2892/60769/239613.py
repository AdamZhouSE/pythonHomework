def solve(num):
    while num != 0:
        count[num % 10] += 1
        num = num // 10


count = []
for i in range(10):
    count.append(0)
m, n = list(map(int, input().split(" ")))
for i in range(m, n + 1):
    solve(i)
print(" ".join(map(str,count)),end="")
