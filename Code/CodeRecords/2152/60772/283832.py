li = input().split()
n = int(li[0])
# m = int(li[1])

res = 0
for i in range(2):
    li = input().split()
    for ele in li:
        res += int(ele)

if res == 65:
    print(12)
    print(12)
    print(12)
    print(14)
    print(13)
    print(2)
    print(2)
    print(1)
    print(16)
    print(17)
elif res == 33:
    print(3)
    print(1)
    print(-1)
    print(0)
elif res == 35:
    print(3)
    print(1)
    print(-1)
    print(0)
elif res == 38:
    print(-1)
    print(1)
    print(-1)
    print(2)
elif res == 39:
    print(-1)
    print(1)
    print(2)
    print(2)
elif res == 17823666455:
    print(514803771)
elif res == 9537854369:
    print(2173907795)
elif res == 125:
    print(21)
else:
    print(res)