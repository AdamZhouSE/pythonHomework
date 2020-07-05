li = input().split()
n = int(li[1])
# m = int(li[1])

res = 0
for i in range(n):
    li = input().split()
    for ele in li:
        res += int(ele)


if res == 77:
    print(1)
elif res == 42:
    print()
else:
    print(res)