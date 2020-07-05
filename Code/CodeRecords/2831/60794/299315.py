aa = input()
a = input().split(" ")
for i in range(len(a)):
    a[i] = int(a[i])
bb = input().split(" ")
b = []
ans1 = 0
ans2 = 0
for i in range(len(bb)):
    b.append(int(bb[i])-1)
for i in range(min(b), max(b)):
    ans1 = ans1 + a[i]
    a[i] = 0
for i in range(len(a)):
    ans2 = ans2 + a[i]
print(min(ans1, ans2))