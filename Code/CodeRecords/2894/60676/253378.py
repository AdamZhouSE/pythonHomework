def most_vk(s):
    res = 0
    index = 0
    while index < len(s)-1:
        if s[index:index+2] == 'VK':
            res += 1
            s = s[:index] + s[index+2:]
            index -= 1
        index += 1
    if len(s) > 1 and s != 'KV':
        res += 1
    return res


a = input()
print(most_vk(input()), end='')