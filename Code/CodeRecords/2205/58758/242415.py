def catalan_number(n):
    n //= 2
    if n == 1:
        return 1
    else:
        result = 1
        for i in range(n+2, 2*n+1):
            result *= i
        for i in range(1, n+1):
            result //= i
        return result


count = int(input())
ans = []
for i in range(0, count):
    num = int(input())
    ans.append(catalan_number(num))
for j in ans:
    print(j)
