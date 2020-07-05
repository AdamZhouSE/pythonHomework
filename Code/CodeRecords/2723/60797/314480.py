if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        res = 0
        for j in range(len(s) - 1, -1, -1):
            tmp = int(s[j])
            if res + tmp < 10:
                res = res + tmp
            else:
                break
        print(res)
