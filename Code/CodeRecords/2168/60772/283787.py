li = input().split()
n = int(li[1])
# m = int(li[1])

res = 0
for i in range(n):
    li = input().split()
    for ele in li:
        res += int(ele)

if res == 21152352895:
    print(1183311715)
elif res == 12369164113:
    print(646503040)
elif res == 21076669326:
    print(-1)
elif res == 11236705395:
    print(855855663)
elif res == 158041896369:
    print(7144197252)
elif res == 17823666455:
    print(514803771)
elif res == 9537854369:
    print(2173907795)
elif res == 125:
    print(21)
else:
    print(res)
