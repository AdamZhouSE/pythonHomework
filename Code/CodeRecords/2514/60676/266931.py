def method(s, t):
    ptr1 = 0
    ptr2 = 0
    while ptr1 < len(s) and ptr2 < len(t):
        if s[ptr1] == t[ptr2]:
            ptr1 += 1
        ptr2 += 1
    if ptr1 == len(s):
        return True
    else:
        return False


if __name__ == '__main__':
    print(method(input(), input()))