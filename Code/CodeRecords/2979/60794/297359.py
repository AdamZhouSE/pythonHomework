a = input().split(" ")
ans = 0
for i in range(len(a)):
    if len(a[i]) > len(a[ans]):
        ans = i
print(a[ans])