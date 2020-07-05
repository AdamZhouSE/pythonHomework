if __name__ == '__main__':
    fomula = input()           #输入公式
    list = fomula.split('+')
    newList = []
    for element in list:
        newList.append(int(element))
    newList.sort()
    print(newList[0], end="")
    for i in range(1,len(newList)):
        print('+' + str(newList[i]), end="")
    print()