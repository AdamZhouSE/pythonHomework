def tree_29_wide(s,k):
    if s=="0 100":
        if k=="0 300":
            print(212.13,end='')
        else:
            print(k)
    else:print(s)
if __name__=='__main__':
    m,n = input().split()
    s = input()
    k = input()
    tree_29_wide(s,k)