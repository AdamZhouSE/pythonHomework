def change(num):
    s = ''
    while num != 0:
        s = chr(num % 26 + 64) + s
        num = int(num / 26)
    s = s.replace('A@', 'Z')
    return s


print(change(int(input())))