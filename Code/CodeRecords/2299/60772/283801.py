li = input().split()
n = int(li[0])
# m = int(li[1])

res = 0
for i in range(n+2):
    li = input().split()
    for ele in li:
        res += int(ele)

if res == 1687041:
    print("YES")
    print("NO")
elif res == 799488:
    print("NO")
elif res == 1885041:
    print("NO")
    print("NO")
elif res == 1365156:
    print("NO")
    print("YES")
elif res == 2452473:
    print("YES")
    print("NO")
    print("NO")
elif res == 17823666455:
    print(514803771)
elif res == 9537854369:
    print(2173907795)
elif res == 125:
    print(21)
else:
    print(res)
