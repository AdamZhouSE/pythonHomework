if __name__ == '__main__':
    chars = [0] * 200
    s = input()
    n = len(s)
    for i in range(n):
        if s[i] != ' ':
            chars[ord(s[i])] += 1
    cnt = 0
    for i in range(200):
        if chars[i] != 0:
            cnt += 1
    print(cnt)