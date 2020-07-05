n = int(input())
a = input().split(" ")
for i in range(0, n):
    a[i] = int(a[i])
a = sorted(a)
print(a[0], end="")
for i in range(1, n):
    print(" " + str(a[i]), end="")
print()