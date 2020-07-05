n = int(input())
a = list(map(int, input().split()))
count = 0
for i in range(n):
    if sum(a[:i]+a[i+1:]) % 2 == 0:
        count += 1
print(count) 