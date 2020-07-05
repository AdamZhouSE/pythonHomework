if __name__=='__main__':
    n = input()
    s = int(n)
    if s>0:
        n = n[::-1]
        print(int(n))
    elif s<0:
        n = n[1:]
        n = n[::-1]
        n = "-"+n
        print(int(n))
    else:
        print(0)