num_test = int(input())
info_list = []
for i in range(num_test):
    info = input().split()
    info = [int(x) for x in info]
    for j in range(info[0]):
        data = input().split()
        data = [int(x) for x in data]
        info_list.append(data)
print(info_list)