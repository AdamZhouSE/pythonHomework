def question15():
    input()
    a = sorted(map(int,input().split(' ')))
    inf = input().split(' ')
    b = []
    result = ''
    for e in inf:
        b.append(int(e))
    for element in b:
        num = 0
        for i in a:
            if i <= element:
                num += 1
        result += str(num) + ' '
    return result.strip(' ')

def question16():

    return

if __name__ == '__main__':
    print(question15())
