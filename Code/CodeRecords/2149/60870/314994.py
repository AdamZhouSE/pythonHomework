info = input().split()
info = [int(x) for x in info]
input_list = [info]
for i in range(info[0] - 1):
    input_str = input().split()
    input_str = [int(x) for x in input_str]
    input_list.append(input_str)
print(input_list)
