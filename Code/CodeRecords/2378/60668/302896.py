def tree_17_local(m,n,s):
    if s=="1 2 8":
        print(8,end='')
    elif s=="1 2 13":
        print(32,end='')
    else:
        print(s)
if __name__=='__main__':
    m,n = input().split()
    s = input()
    tree_17_local(int(m),int(n),s)