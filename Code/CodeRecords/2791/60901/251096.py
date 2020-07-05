def question16():
    num = int(input())
    step = input().split(' ')
    list = []
    for e in step:
        list.append(int(e))
    newList = []
    for i in range(0, num):
        if i == num - 1:
            newList.append(list[i])
        elif list[i+1] <= list[i]:
            newList.append(list[i])
    print(len(newList))
    print(newList[0], end='')
    for i in range(1, len(newList)):
        print(' ' + str(newList[i]),end='')
    print()
    return

if __name__ == '__main__':
    question16()
