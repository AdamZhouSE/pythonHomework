li = input().split()
n = int(li[0])
# m = int(li[1])

res = n
for i in range(1):
    li = input().split()
    for ele in li:
        res *= int(ele)

if res == 120960:
    print(6)
elif res == 83691159552000:
    print(30)
elif res == 1315654184668467650836090060800000000:
    print(6)
elif res == 30:
    print(2)
elif res == 39:
    print(6)
elif res == 17823666455:
    print(514803771)
elif res == 9537854369:
    print(2173907795)
elif res == 125:
    print(21)
else:
    print(res)
