s = input().split(" ")
n = int(s[0])
m = int(s[1])
a = input().split(" ")
b = input().split(" ")
count = 0
for i in range(0, m):
    count = 0
    for j in range(0, n):
        if int(a[j]) <= int(b[i]):
            count += 1
    if i == 0:
        print(str(count), end="")
    else:
        print(" "+str(count), end="")
print()