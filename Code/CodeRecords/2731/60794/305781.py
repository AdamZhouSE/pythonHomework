num = int(input())
for i in range(num):
    pp = input()
    aa = input().split(" ")
    a = []
    for j in range(len(aa)):
        a.append(int(aa[i]))
    list.sort(a)
    for j in range(len(a)-1):
        if a[j] == a[j+1]:
            a[j] = -1
            a[j+1] = -1
    ans = 0
    for j in range(len(a)):
        if a[j] == -1:
            ans = ans + 1
    print(ans)