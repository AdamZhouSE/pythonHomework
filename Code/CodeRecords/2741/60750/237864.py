import ast


def longest(data):
    temp_res = []
    i = 0
    length = []
    max_len = 0
    temp = 1
    while i < len(data):
        if i == len(data) -1:
            i = i + 1
            length.append(temp)
        elif data[i] < data[i + 1]:
            i = i + 1
            temp = temp + 1
        else:
            length.append(temp)
            temp = 1
            i = i + 1
    for i in range(0,len(length)):
        if length[i] > max_len:
            max_len = length[i]
    return max_len


data = ast.literal_eval(input())
print(longest(data))