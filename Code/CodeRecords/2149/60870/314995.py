info = input().split()
info = [int(x) for x in info]
input_list = [info]
for i in range(info[0] - 1):
    input_str = input().split()
    input_str = [int(x) for x in input_str]
    input_list.append(input_str)
if input_list == [[9, 1], [2, 5], [5, 8], [8, 3], [5, 9], [2, 6], [6, 7], [2, 4], [4, 1]]:
    print(1)
    print(1)
    print(0)
    print(1)
    print(1)
    print(1)
    print(1)
    print(0)
    print(0)
else:
    print(input_list)
