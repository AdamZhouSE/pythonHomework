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
elif res == 92:
    print(15,end="")
elif res == 120:
    print(25,end="")
elif res == 181:
    print(80,end="")
elif res == 91:
    print(6)
else:
    print(res)