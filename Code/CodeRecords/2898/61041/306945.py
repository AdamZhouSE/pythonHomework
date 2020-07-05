if __name__ == '__main__':
    n = input()
    string = input()
    re = "1"
    for i in range(len(string)):
        if string[i] == '0':
            re = re + "0"
    print(re,end='')