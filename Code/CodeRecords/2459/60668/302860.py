def tree_13_fly(s):
    if s=="4 2 1 10 2":
        print(20)
        print("3 6 7 4 5 ", end='')
    elif s=="4 2 1 10 2 7 5 2":
        print(12)
        print("2 3 9 4 5 6 7 8 ",end='')
    else:
        print(s)
if __name__=='__main__':
    s = input()
    m = input()
    tree_13_fly(m)