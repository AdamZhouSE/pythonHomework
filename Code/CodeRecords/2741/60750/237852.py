import ast


def longest(data):
    temp_res = []
    i = 0
    while i < len(data):
        temp = [data[i]]
        while i < len(data) - 1:
            if data[i] < data[i + 1]:
                temp.append(data[i + 1])
                i = i + 1
                if i == len(data) - 1:
                    i = i + 1
            else:
                i = i + 1
                break
        temp_res.append(temp)
    max_len = 0
    max_index = 0
    for i in range(0,len(temp_res)):
        if len(temp_res[i]) > max_len:
            max_index = i
            max_len = len(temp_res[i])
    return max_len


data = ast.literal_eval(input())
print(longest(data))