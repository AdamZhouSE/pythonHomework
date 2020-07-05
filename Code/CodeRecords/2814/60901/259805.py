def question28():
    num = int(input())
    l = list(map(int, input().split()))
    l.sort()
    saitisfied = 0
    index = 0
    while not num == 0:
        if sum(l[:index])<=l[index]:
            saitisfied += 1
            index += 1
        else:
            del l[index]
        num -= 1

    return saitisfied

if __name__ == '__main__':
    print(question28())