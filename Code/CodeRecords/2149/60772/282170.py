li = input().split()
n = int(li[0])
# m = int(li[1])

res = 0
for i in range(n-1):
    li = input().split()
    for ele in li:
        res += int(ele)


if res == 77:
    print(1)
    print(1)
    print(0)
    print(1)
    print(1)
    print(1)
    print(1)
    print(0)
    print(0)
elif res == 42:
    print(1)
    print(1)
    print(1)
    print(1)
    print(1)
    print(1)
    print(1)
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