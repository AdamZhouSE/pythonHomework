def i(s,n):
    try:
        while s[-1]==str(n):
            s=s[:-1]
    except IndexError:
        return 0
    return i(s,n^1)+1
if __name__ == '__main__':
    print(i(input(),1),end='')