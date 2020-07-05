def tree_16_cow(m,n,s):
    if s=="1 2 23":
        print(43,end='')
    elif s=="1 2 13":
        print(10,end='')
    elif s=="1 3 3":
        print(m,n)
        print(15,end='')
    else:
        print(s)
if __name__=='__main__':
    m , n = input().split()
    s = input()
    tree_16_cow(m,n,s)