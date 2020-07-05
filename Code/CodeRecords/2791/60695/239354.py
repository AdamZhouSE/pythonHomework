n = int(input())
a = input().split(" ")
count = 0
for i in range(0, n):
    if a[i] == "1":
        count += 1
print(count)
for i in range(0, n):
    if i == n-1:
        print(a[i])
    elif a[i + 1] == "1":
        print(a[i] + " ", end="")