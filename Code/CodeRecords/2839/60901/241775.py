def question11():
    num = int(input())
    list = []
    for i in range(0,num):
        name = input()
        if list.__contains__(name):
            print('YES')
        else:
            print('NO')
        list.append(name)
    return 

if __name__ == '__main__':
    question11()