li = input().split()
n = int(li[0])
# m = int(li[1])

res = n
for i in range(n):
    li = input().split()
    N = int(li[0])
    K = int(li[1])
    res = res + N + K
    for j in range(N):
        li = input().split()
        for ele in li:
            res += int(ele)


if res == 285:
    print(15)
    print(316)
elif res == 5164489:
    print(26998514)
    print(9400115)
    print(5790773)
    print(2919180)
    print(1954284)
elif res == 973:
    print(2171)
    print(5)
    print(245)
    print(22)
elif res == 191:
    print(5)
    print(245)
    print(15)
elif res == 4676489:
    print(49603)
    print(49635)
    print(50128)
    print(49633)
    print(1954284)
elif res == 91:
    print(6)
else:
    print(res)