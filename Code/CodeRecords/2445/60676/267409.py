def letter_ectopic(s, t):
    if len(s) != len(t):
        return 'false'
    ele1 = list(s)
    ele2 = list(t)
    ele1.sort()
    ele2.sort()
    if ele1 == ele2:
        return 'true'
    return 'false'


if __name__ == '__main__':
    a = input().split('"')
    print(letter_ectopic(a[1], a[3]))