n = int(input())
a = int(input())
b = int(input())
c = int(input())
k = min(a, b, c)
i = 1
while i < n:
    k = k + 1
    if k % a == 0 or k % b == 0 or k % c == 0:
        i = i + 1
print(k)