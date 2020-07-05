n = int(input())
h = input().split(" ")
for i in range(0, n):
    h[i] = int(h[i])
h = sorted(h)
print(h[n-1])