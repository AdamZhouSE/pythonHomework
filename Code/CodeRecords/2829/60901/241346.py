def question9():
    num = int(input())
    inf = input().split(' ')
    list = []
    for e in inf:
        list.append(int(e))
    list.sort()
    num1 = list[len(list)-2] - list[0]
    num2 = list[len(list)-1] - list[1]
    return min(num1, num2)

if __name__ == '__main__':
    print(question9())