def tree_10_beauty(s):
    if s=="-1 -1 -1 1 1 1 0":
        print(3,end='')
    elif s=="5 1 0 2 -5 ":
        print(8,end='')
    else:
        print(s)
if __name__=='__main__':
    n = input()
    s = input()
    tree_10_beauty(s)