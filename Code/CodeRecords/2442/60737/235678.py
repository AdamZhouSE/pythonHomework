def get_dvalue(s):
    if len(s) < 2:
        return 0
    s.sort()
    dvalue = 0
    for i in range(0, len(s)-1):
        if s[i+1]-s[i] > dvalue:
            dvalue = s[i+1]-s[i]
    return dvalue


if __name__ == "__main__":
    s = [int(n) for n in input()[1:-1].split(',')]
    print(get_dvalue(s))
