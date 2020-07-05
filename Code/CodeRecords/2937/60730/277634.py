temp = list(input())
a = list("CODEFESTIVAL2016")
ans = 0
for i in range(len(a)):
    if a[i] != temp[i]:
        ans += 1
print(ans)
