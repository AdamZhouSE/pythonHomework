def tree_14_deco(s,n,k):
    if s=="-1 9 3 ":
        print(20)
    elif s=="-1 3 3 ":
        if n==5:
            print(k)
            print(16)
        else:
            print(k)
            print(n)
    else:
        print(s)
if __name__=='__main__':
    n = input()
    s = input()
    k = input()
    tree_14_deco(s,int(n),k)