if __name__ == '__main__':
    s = input()
    n = len(s)
    cnt = 0
    for i in range(128):
        if s[i] != ' ':
            cnt += 1
    print(cnt)