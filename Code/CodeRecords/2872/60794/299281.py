aa = input()
a = list(input())
ans = 0
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        ans = ans + 1
print(ans)