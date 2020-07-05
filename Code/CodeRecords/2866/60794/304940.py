aa = input()
aaa = input().split(" ")
a = []
for i in range(len(aaa)):
    a.append(int(aaa[i]))
gap = []
for i in range(len(a)):
    if a[i] == 1:
        gap.append(i)
ans = 1
if len(gap) == 1:
    print(1)
elif len(gap) == 0:
    print(0)
else:
    for i in range(len(gap)-1):
        ans = ans * (gap[i+1]-gap[i])
    print(ans)