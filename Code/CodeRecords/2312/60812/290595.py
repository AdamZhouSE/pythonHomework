def count(n, d: dict):
    sum = 0
    for i in range(n):
        if i not in d:
            d[i] = count(i, d)
        temp = n-1-i
        if temp not in d:
            d[temp] = count(temp, d)
        sum += d[i]*d[temp]
    return sum


n = int(input())
d = {0: 1, 1: 1}
print(count(n, d)%(1000000007))