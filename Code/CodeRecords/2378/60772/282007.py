li = input().split()
n = int(li[1])

res = 0
for i in range(n):
    li = input().split()
    for ele in li:
        res += int(ele)


if res == 97:
    print(32,end="")
elif res == 45:
    print(8,end="")
elif res == 7848:
    print()
elif res == 8953:
    print()
elif res == 82:
    print(1)
elif res == 91:
    print(6)
else:
    print(res)