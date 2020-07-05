def is_valid(num_str):
    num_str = num_str.replace(' ', '')
    if 'e' in num_str:
        a = num_str.split('e')
        if len(a) > 2:
            return False
        return is_valid(a[0]) and is_valid(a[1])
    if '.' in num_str:
        b = num_str.split('.')
        if len(b) > 2:
            return False
        return is_valid(b[0]) and is_valid(b[1])
    for i in range(len(num_str)):
        if not num_str[i].isnumeric():
            return False
    return True


print(is_valid(input()))