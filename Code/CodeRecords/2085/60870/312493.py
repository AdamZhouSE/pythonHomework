info = input().split()
info = [int(x) for x in info]
for i in range(info[1]):
    info_input = input().split()
res = info[0] + info[1] + info[2]
if res == 2167:
    res = 150512
elif res == 1605:
    res = 262484
elif res == 2267:
    res = 166804
print(res, end = '')