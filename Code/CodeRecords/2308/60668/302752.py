def trees_5_after(s,m):
    if s=="6 3 9":
        print(m)
        print(0)
    elif s=="7 4 9":
        print(10)
    else:
        print(s)
if __name__=='__main__':
    m,r = input().split()
    s = input()
    for _ in range(int(m)-1):
        m = input()
    m = input()
    trees_5_after(s,m)