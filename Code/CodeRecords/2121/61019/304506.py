read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

n = read()
if n > 10:
    n = 10
cnt = 0
fact = lambda x: 1 if x <= 1 else x * fact(x - 1)
for i in range(1, n + 1):
    c = 9 * fact(9) // fact(10 - i)
    cnt += c
print(cnt + 1)
