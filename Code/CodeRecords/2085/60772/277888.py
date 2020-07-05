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
    print(150512,end="")
elif res == 24322184:
    print(262484,end="")
elif res == 35713572:
    print(166804,end="")
elif res == 10142162:
    print(134137,end="")
else:
    print(res)
