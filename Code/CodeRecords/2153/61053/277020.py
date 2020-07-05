def reverse(str):
    if str[0] != '-':
        return str[::-1]
    else:
        str = str[1::]
        str = str[::-1]
        str = '-' + str
        return str

if __name__ == "__main__":
    str = input()
    print(reverse(str))