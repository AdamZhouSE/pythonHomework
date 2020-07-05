num = int(input())
for i in range(num):
    pp = input()
    aa = input().split(" ")
    a = []
    for j in range(len(aa)):
        a.append(list(aa[j]))
    ans = 0
    for j in range(len(a)):
        for k in range(len(a[j])):
            ans = ans + int(a[j][k])
    if ans % 3 == 0:
        print(1)
    else:
        print(0)