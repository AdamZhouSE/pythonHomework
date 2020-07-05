def question7():
    num = int(input())
    list = []
    for i in range(0, num):
        inf = input().split(' ')
        grades = map(int, inf)
        list.append(sum(grades))
    grade = list[0]
    list.sort()
    for i in range(len(list)-1, -1, -1):
        if grade == list[i]:
            return num - i

if __name__ == '__main__':
    print(question7())