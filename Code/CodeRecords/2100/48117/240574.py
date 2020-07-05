def factorial(n : int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input())
n1 = str(factorial(n))

count0 = 0
for num in n1:
    if num == '0':
        count0 += 1

print(count0)