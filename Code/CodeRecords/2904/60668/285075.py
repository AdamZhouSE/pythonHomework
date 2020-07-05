if __name__=='__main__':
    n = input()
    s = int(n)
    if s>0:
        n = n[::-1]
        print(n)
    else:
        n = n[1:]
        n = n[::-1]
        m = int(n)
        m = 0-m
        print(m)