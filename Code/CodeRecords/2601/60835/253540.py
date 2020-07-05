m = int(input())
n = int(input())
k = int(input())
result = []
cnt = 2
while len(result) < k:
    for x in range(1,cnt):
        if x <= m and cnt-x <= n:
            result.append(x*(cnt - x))
    cnt = cnt + 1
result.sort()
print(result[k-1])