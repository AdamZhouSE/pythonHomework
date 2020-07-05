num_str = input()
if(num_str[0] == '-'):
    print('-' + (num_str[1:])[::-1])
else:
    print(num_str[::-1])