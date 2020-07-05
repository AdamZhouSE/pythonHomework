aa = input()
a = input().split(" ")
b = input().split(" ")
ans = []
for i in range(len(a)):
    for k in range(len(b)):
        if a[i] == b[k]:
            ans.append(a[i])
for i in range(len(ans)-1):
    print(ans[i] + " ", end="")
print(ans[len(ans)-1])