n = int(input())
origin = list(map(str, input().split(' ')))
now = list(map(str, input().split(' ')))
result = 0
for i in range(n):
    for j in range(i + 1, n):
        a, b = origin[i], origin[j]
        past = origin.index(a) - origin.index(b)
        present = now.index(a) - now.index(b)
        if past * present < 0:
            result += 1
print(result)
