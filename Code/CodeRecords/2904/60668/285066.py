if __name__=='__main__':
    n = input()
    s = int(n)
    if s>0:
        n = reversed(n)
    else:
        n = reversed(n[1:])
        n = '-'+n
    print(int(n))