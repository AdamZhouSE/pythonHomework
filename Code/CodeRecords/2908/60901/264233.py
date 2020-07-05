def question1():
    num = int(input())
    l = []
    for i in range(num):
        string = input().strip(' ')
        l.append(str(sorted(list(string))))
    return len(list(set(l)))

if __name__ == '__main__':
    print(question1(),end = '')