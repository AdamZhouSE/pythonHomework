def question12():
    num = int(input())
    list = map(int,input().split(' '))
    codes = sorted(list)
    newList = []
    for code in codes:
        if not newList.__contains__(code) and not code == 0:
            newList.append(code)
    return len(newList)

if __name__ == '__main__':
    print(question12())
