n = int(input())
a = input().split(" ")
a = list(map(int, a))
cnt = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if a[i] < a[j] and a[j] < a[k]:
                cnt += 1
print(cnt,end="")
