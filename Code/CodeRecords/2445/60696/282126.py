def solve(s, t):
    letter1 = [0 for i in range(30)]
    letter2 = [0 for i in range(30)]
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        letter1[ord(s[i]) - ord('a')] += 1
        letter2[ord(t[i]) - ord('a')] += 1
    for i in range(len(letter1)):
        if letter1[i] != letter2[i]:
            return False
    return True


if __name__ == '__main__':
    arr = input()[5:-1]
    i = arr.find('"')
    s = arr[:i]
    t = arr[i+8:]
    if solve(s, t):
        print('true')
    else:
        print('false')
