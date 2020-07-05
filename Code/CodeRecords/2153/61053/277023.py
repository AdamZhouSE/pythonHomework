def reverse(str):
    if str[0] != '-':
        str = str[::-1]
        index = 0
        while str[index] == '0':
            index += 1
        str = str[index::]
        return str
    else:
        str = str[1::]
        str = str[::-1]
        index = 0
        while str[index] == '0':
            index += 1
        str = str[index::]
        str = '-' + str
        return str

if __name__ == "__main__":
    str = input()
    print(reverse(str))