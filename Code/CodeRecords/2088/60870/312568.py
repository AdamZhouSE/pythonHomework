num = int(input())
info_list = []
for i in range(num - 1):
    info = input().split()
    info_list.append(info)
res = num * info_list[0][0]
print(res)