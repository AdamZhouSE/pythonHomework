t = int(input())
result = []
for i in range(t):
    n = int(input())
    tmp = str(n % 9) + '9' * (n // 9) + '0' * n
    result.append(tmp)
for i in result:
    print(i)
