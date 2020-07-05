def question29():
    num = int(input())
    l = list(map(int, input().split()))
    while True:
        if len(l) == 1:
            return l[0]
        del(l[l.index(max(l))])
        if len(l) == 1:
            return l[0]
        del(l[l.index(min(l))])

if __name__ == '__main__':
    print(question29())