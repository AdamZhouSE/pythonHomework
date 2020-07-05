n, m = list(map(int, input().split()))

result = list(range(1, n+1))
for i in range(m):
    a, b = list(map(int, input().split()))
    result = result[:a-1] + result[a-1:b][::-1] + result[b:]
print(' '.join(list(map(str, result))), end=' ')