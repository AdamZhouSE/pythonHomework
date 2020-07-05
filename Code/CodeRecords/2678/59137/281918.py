def s5():
    t = int(input())
    for i in range(t):
        n = int(input())
        s = bin(n)[2:]
        flag = 0
        index = -1

        for i in range(len(s)):
            if flag == 0 and s[i] == '1':
                flag = 1
                index = len(s) - i
            elif flag == 1 and s[i] == '1':
                flag = 2
                break
        if flag != 1:
            print(-1)
        else:
            print(index)


s5()