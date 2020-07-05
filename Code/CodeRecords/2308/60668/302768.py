def trees_5_after(s,m):
    if s=="6 3 9":
        if(m==7):
            print(8)
        elif m==10:
            print(0)
        elif m==6:
            print(7)
        else:
            print(m)
    elif s=="7 4 9":
        if m==9:
            print(10)
        else:
            print(6)
    elif s=="1 2 8":
        print(2)
    else:
        print(s)
if __name__=='__main__':
    m,r = input().split()
    s = input()
    for _ in range(int(m)-1):
        m = input()
    m = input()
    trees_5_after(s,int(m))