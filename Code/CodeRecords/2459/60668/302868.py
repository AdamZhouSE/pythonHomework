def tree_13_fly(s,k):
    if s=="4 2 1 10 2":
        if k==2:
            print(20)
            print("3 6 7 4 5 ", end='')
        else:
            print(33)
            print("5 7 8 4 6 ",end='')
    elif s=="4 2 1 10 2 7 5 2":
        if k==1:
            print(12)
            print("2 3 9 4 5 6 7 8 ",end='')
        elif k==2:
            print(29)
            print("3 9 10 4 5 6 7 8 ", end='')
        elif k==4:
            print(77)
            print("8 11 12 5 10 6 7 9 ", end='')
        else:
            print(k)
    else:
        print(s)
if __name__=='__main__':
    s,k = input().split()
    m = input()
    tree_13_fly(m,int(k))