class Name:
    def __init__(self, s, sign=0):
        self.s = s
        self.sign = sign


if __name__ == '__main__':
    names = []
    n = int(input())
    for i in range(n):
        names.append(Name(input()))
    m = int(input())
    for i in range(m):
        s = input()
        is_wrong = True
        for j in range(n):
            if names[j].s == s:
                if names[j].sign == 0:
                    print('OK')
                    is_wrong = False
                    names[j].sign = 1
                else:
                    is_wrong = False
                    print('REPEAT')
                break
        if is_wrong:
            print('WRONG')