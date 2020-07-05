def find(n):
    if n <= 1:
        return 1
    else:
        result = [0]*(n+1)
        result[0] = 1
        for i in range(1,n+1):
            for j in range(1,i+1):
                result[i] += result[j-1] * result[i-j]
    return result[n]

n = int(input())
result = find(n)
print(result % (10**9+7))