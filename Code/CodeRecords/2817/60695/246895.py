n = int(input())
a = input().split(" ")
flag = False
for i in range(0, n):
    if a[int(a[int(a[int(a[i])-1])-1])-1] == a[i]:
        flag = True
if flag:
    print("YES")
else:
    print("NO")