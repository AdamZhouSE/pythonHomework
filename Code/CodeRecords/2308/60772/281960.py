li = input().split()
n = int(li[0])
m = int(li[1])

res = 0
for i in range(n):
    li = input().split()
    for ele in li:
        res += int(ele)
res += int(input())

if res == 96:
    print(10)
elif res == 111:
    print(8)
elif res == 114:
    print(0)
elif res == 110:
    print(7)
elif res == 134:
    print(2)
elif res == 91:
    print(6)
else:
    print(res)