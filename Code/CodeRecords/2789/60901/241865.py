def question14():
    num = int(input())
    lengthes = sorted(map(int, input().split(' ')))
    result = []
    for i in range(0, num):
        if lengthes[i] >= num - i:
            result.append(num-i)
    return max(result)

if __name__ == '__main__':
    test = int(input())
    for i in range(0,test):
        print(question14())
