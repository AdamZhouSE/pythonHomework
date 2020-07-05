num_test = int(input())
info_list = []
for i in range(num_test):
    info = input().split()
    info = [int(x) for x in info]
    for j in range(info[0] - 1):
        edge = input().split()
        edge = [int(x) for x in edge]
        info_list.append(edge)
print(info_list)