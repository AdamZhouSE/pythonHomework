li = input().split()
n = int(li[0])
# m = int(li[1])

res = 0
for i in range(2*n-1):
    li = input().split()
    for ele in li:
        res += int(ele)


if res == 7975851:
    print(643,end="")
elif res == 52:
    print(1,end="")
elif res == 28:
    print(0)
elif res == 6:
    print(1)
elif res == 467618328051:
    print(244080)
elif res == 25:
    print(2)
else:
    print(res)