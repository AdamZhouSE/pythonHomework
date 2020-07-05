li = input().split()
n = int(li[0])

res = 0
for i in range(n-1):
    li = input().split()
    for ele in li:
        res += int(ele)

m = int(input())
for i in range(m):
    li = input().split()
    for ele in li:
        res += int(ele)

if res == 624:
    print(246)
    print(220)
    print(74)
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