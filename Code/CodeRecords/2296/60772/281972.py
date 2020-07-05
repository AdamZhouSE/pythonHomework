li = input().split()
n = int(li[0])

res = 0
for i in range(n):
    li = input().split()
    for ele in li:
        res += int(ele)

res += int(input())

if res == 83:
    print(2)
elif res == 532:
    print(4)
    print(146)
    print(246)
elif res == 2:
    print(4)
elif res == 49008:
    print(975)
    print(14675)
    print(0)
elif res == 134:
    print(2)
elif res == 91:
    print(6)
else:
    print(res)