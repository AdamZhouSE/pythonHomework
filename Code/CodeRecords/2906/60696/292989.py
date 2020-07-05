def find_pwd(s, n):
    res = ''
    for i in range(len(s)):
        res += chr(ord('a') + (ord(s[i])-ord('a')+n) % 26)
    return res


if __name__ == '__main__':
    n = int(input())
    s = input()
    print(find_pwd(s, n), end='')