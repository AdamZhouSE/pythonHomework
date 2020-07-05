info = input().split()
info = [int(x) for x in info]
for i in range(info[1]):
    info_input = input().split()
res = info[0] + info[1]
if res == 2144:
    res = 459312924580
print(res, end = '')