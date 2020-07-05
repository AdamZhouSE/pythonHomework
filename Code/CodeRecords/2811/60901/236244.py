def question2():
    information = input().split(' ')
    p = int(information[0])
    n = int(information[1])
    list = []
    for i in range(0, n):
        x = int(input())
        position = x % p
        if list.__contains__(position):
            return len(list) + 1
        list.append(position)
    return -1

if __name__ == '__main__':
    print(question2())
