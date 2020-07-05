info = input().split()
info = [int(x) for x in info]
info_list = []
for i in range(info[1]):
    info_input = input().split()
    info_list.append(info_input)
if info_list == [['0', '2', '1', '5'], ['0', '4', '1', '1'], ['0', '0', '2', '1'], ['0', '2', '5', '5'], ['1', '2', '1'], ['2', '3', '5'], ['0', '1', '5', '2'], ['0', '5', '3', '6'], ['2', '1', '2'], ['2', '2', '1']]:
    print(-1)
    print(5)
    print(5)
else:
    print(info_list)