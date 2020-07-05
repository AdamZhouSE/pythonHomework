def question8():
    num = int(input())
    inf = input().split(' ')
    list = []
    for e in inf:
        list.append(int(e))
    list.sort()
    print(list[0], end= '')
    for i in range(1, num):
        print(' ' + str(list[i]),end = '')
    print()

if __name__ == '__main__':
    question8()