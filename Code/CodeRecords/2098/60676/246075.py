def transformer(num):
    length = 1
    copy = num
    while copy > 26:
        length += 1
        copy %= 26
    res = ''
    copy = num
    for i in range(length):
        res += chr(ord('A') + copy // pow(26, length-i-1) - 1)
        copy %= pow(26, length-i-1)
    return res


print(transformer(int(input())))