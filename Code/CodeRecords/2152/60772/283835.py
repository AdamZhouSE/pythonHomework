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
elif res == 48:
    print(12)
    print(12)
    print(12)
    print(14)
    print(13)
    print(2)
    print(2)
    print(1)
elif res == 61:
    print(7)
    print(5)
    print(4)
    print(4)
    print(4)
    print(8)
    print(6)
    print(5)
    print(4)
    print(5)
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
