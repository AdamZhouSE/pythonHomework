if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        patt = input()
        isover = 0
        for i in range(len(s)):
            if s[i] in set(patt):
                print(s[i])
                isover = 1
                break
        if not isover:
            print('$')