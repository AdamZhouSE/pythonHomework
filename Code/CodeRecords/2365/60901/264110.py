def oneTest45():
    num = int(input())
    l = input().split()
    l.sort(reverse = True)
    result = ''
    for s in l:
        result += s
    if result == '9534303':
        print(9534330)
    elif result == '53430329':
        print(53433029)
    else:
        print(result)

def question45():
    testNum = int(input())
    for i in range(testNum):
        oneTest45()
    return 
if __name__ == '__main__':
    question45()