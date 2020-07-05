def huiwen():
    num = input()
    new = num[-1::-1]
    return num == new


print(huiwen())