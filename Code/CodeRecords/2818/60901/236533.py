def question4():
    inf = input().split(' ')
    init = int(inf[1])
    chapters = input().split(' ')
    list = []
    for element in chapters:
        list.append(int(element))
    list.sort()
    init += 1
    result = 0
    for chapter in list:
        if init > 1:
            init -= 1
        result += chapter * init
    return result

if __name__ == '__main__':
    print(question4())
