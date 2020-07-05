def ap(s):
    # TODO
    d=(0,1)
    l=(0,0)
    for _ in range(8):
        for i in s:
            d,l=ap_1(d,l,i)
        if l==(0,0):
            print(True)
    print(False)
def ap_1(d,l,c):
    if c=='G':
        return d,(l[0]+d[0],l[1]+d[1])
    elif c=='L':
        if d==(0,1):
            return (-1,0),l
        elif d==(-1,0):
            return (0,-1),l
        elif d==(0,-1):
            return (1,0),l
        elif d==(1,0):
            return (0,1),l
    elif c=='R':
        if d==(0,1):
            return (1,0),l
        elif d==(1,0):
            return (0,-1),l
        elif d==(0,-1):
            return (-1,0),l
        elif d==(-1,0):
            return (0,1),l

if __name__ == '__main__':
    ap(input())
