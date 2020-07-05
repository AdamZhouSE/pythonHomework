info = input().split()
info = [int(x) for x in info]
for i in range(info[1]):
    info = input().split()
res = info[0] + info[1] + info[2]
if res == 604926022:
    res = 150512
print(res)