def question18():
    num = int(input())
    list = sorted(map(int, input().split()))
    operation = []
    base = list[0]
    for i in list:
        operation.append(i/base)
    aim = set(operation)
    s = set()
    for i in range(0, 100):
        for j in range(0, 100):
            s.add(pow(2, i)*pow(3, j))
            s.add(pow(2, i) * pow(3, -j))
            s.add(pow(2, -i) * pow(3, j))
            s.add(pow(2, -i) * pow(3, -j))
    if aim.issubset(s):
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    print(question18())