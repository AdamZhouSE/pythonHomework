aa = input()
a = input().split(" ")
ans = [0]*len(a)
for i in range(len(a)):
    a[i] = int(a[i])
for i in range(len(a)):
    ans[a[i]-1] = i + 1
for i in range(len(ans)-1):
    print(ans[i], "", end="")
print(ans[len(ans)-1])