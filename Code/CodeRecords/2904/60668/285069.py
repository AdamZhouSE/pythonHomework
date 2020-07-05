if __name__=='__main__':
    n = input()
    s = int(n)
    if s>0:
        n = reversed(n)
        print(int(n))
    else:
        n = reversed(n[1:])
        print(0-int(n))