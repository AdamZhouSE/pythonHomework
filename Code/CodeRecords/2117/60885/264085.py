def turnN(n):
    result = 0
    for i in range(1,n+1):
        count = 0
        for j in range(1,n+1):
            if i % j == 0:
                count += 1
        if count % 2 == 1:
            result += 1
    return result

n = int(input())
result = turnN(n)
print(result)