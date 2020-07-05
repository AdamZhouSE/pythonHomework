aa = input()
a = input().split(" ")
ans = 0
for i in range(len(a)):
    ans = ans + abs(int(a[i]))
print(ans)