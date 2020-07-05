def reverse():
    num = input()
    a = int(num) > 0
    if not a:
        num = num[1:]
    num = int(num[-1::-1])
    if not a:
        num *= -1
    return num


print(reverse())