n = int(input())
result = [1, n-1]
while True:
    if '0' in str(result[0]) or '0' in str(result[1]):
        result[0] = result[0] + 1
        result[1] = result[1] - 1
    else:
        break
print(result)        