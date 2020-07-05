def question3():
    string = input()
    base = 'CODEFESTIVAL2016'
    diff = 0
    for i in range(16):
        if not string[i] == base[i]:
            diff += 1
    return diff

if __name__ == '__main__':
    print(question3())