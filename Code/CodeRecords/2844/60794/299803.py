spare1 = int(input().split(" ")[1])
a = input().split(" ")
for i in range(len(a)):
    a[i] = int(a[i])
t = 0
for i in range(len(a)):
    ans = 0
    spare = spare1
    for j in range(i+1, len(a)):
        spare = spare - a[j]
        ans = ans + 1
        if spare < 0:
            ans = ans - 1
            break
    if t < ans:
        t = ans
print(t)