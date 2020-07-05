def question24():
    inf = input().split()
    caseNum = int(inf[0])
    keyNum = int(inf[1])
    cases = list(map(int, input().split()))
    keys = list(map(int, input().split()))
    evenCase = 0
    evenKey = 0
    for i in cases:
        if i % 2 == 0:
            evenCase += 1
    for i in keys:
        if i % 2 == 0:
            evenKey += 1
    oddCase = caseNum - evenCase
    oddKey = keyNum - evenKey
    return min(oddCase,evenKey)+min(evenCase,oddKey)

if __name__ == '__main__':
    print(question24())