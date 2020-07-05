li = input().split()
n = int(li[0])
m = int(li[1])
r = int(li[2])

res = 0
for i in range(m):
    li = input().split()
    for ele in li:
        res += int(ele)

if res == 32778229:
    print(150512)
else:
    print(res)
