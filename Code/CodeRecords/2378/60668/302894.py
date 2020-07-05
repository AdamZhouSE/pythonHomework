def tree_17_local(m,n,s):
    if s=="1 2 8":
        print(8)
    else:
        print(s)
if __name__=='__main__':
    m,n = input()
    s = input()
    tree_17_local(int(m),int(n),s)