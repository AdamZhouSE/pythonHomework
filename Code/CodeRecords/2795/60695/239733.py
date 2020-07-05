n = int(input())
a = input().split(" ")
a = sorted(a)
i = 1
while i < n:
    if a[i] == a[i-1]:
        a.remove(a[i])
        n -= 1
    else:
        i += 1
len = len(a)
flag = True
if len == 1:
    print(a[0])
elif len == 2:
    bias0 = int(a[1]) - int(a[0])
    if bias0 % 2 == 0:
        print(int(bias0/2))
    else:
        print(bias0)
else:
    bias0 = int(a[1]) - int(a[0])
    for i in range(1, len):
        bias = int(a[i]) - int(a[i-1])
        if bias != bias0:
            flag = False
    if flag:
        print(bias)
    else:
        print("-1")