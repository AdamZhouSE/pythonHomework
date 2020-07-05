a = input()
b = list(input())
ans = []
for i in range(len(a)):
    for j in range(len(b)):
        if b[j] == a[i]:
            ans.append(b[j])
for i in range(len(b)):
    x = 0
    for j in range(len(a)):
        if b[i] == a[j]:
            x = 1
    if x == 0:
        ans.append(b[i])
print("".join(ans))