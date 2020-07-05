def transformer(num_str):
    negative = False
    index = 0
    if num_str[0] == '-':
        negative = True
        index = 1
    res = 0
    for i in range(index, len(num_str)):
        res *= 10
        if num_str[i] == '1':
            res += 1
        elif num_str[i] == '2':
            res += 2
        elif num_str[i] == '3':
            res += 3
        elif num_str[i] == '4':
            res += 4
        elif num_str[i] == '5':
            res += 5
        elif num_str[i] == '6':
            res += 6
        elif num_str[i] == '7':
            res += 7
        elif num_str[i] == '8':
            res += 8
        elif num_str[i] == '9':
            res += 9
    return res


print(transformer(input()) * transformer(input()))