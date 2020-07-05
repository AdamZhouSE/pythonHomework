num_str = input()
if(num_str[0] == '-'):
    num_str = (num_str[1:])[::-1]
    for i in range(0, len(num_str) - 1):
        if num_str[i] is not '0':
            print('-' + num_str[i:])
            break
else:
    num_str = num_str[::-1]
    for i in range(0, len(num_str) - 1):
        if num_str[i] is not '0':
            print(num_str[i:])
            break