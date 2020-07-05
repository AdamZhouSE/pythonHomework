def letter_ectopic(s, t):
    if len(s) != len(t):
        return False
    ele1 = []
    ele2 = []
    for i in range(len(s)):
        ele1.append(s[i])
        ele2.append(t[i])
    if any(ele1) == any(ele2):
        return True
    return False


if __name__ == '__main__':
    a = input().split('"')
    print(letter_ectopic(a[1], a[3]))