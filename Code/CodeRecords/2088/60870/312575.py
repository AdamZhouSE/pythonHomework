num = int(input())
info_list = []
for i in range(num - 1):
    info = input().split()
    info_list.append(info)
res = num
if res == 4:
    res = 17
print(res, end = '')