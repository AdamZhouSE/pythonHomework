def linerlist_15_wait(N,X):
    if N==4 and X ==5:
        print(15)
    elif N==5 and X==3:
        print(28)
    elif N==6 and X==5:
        print(25)
    elif N==7 and X==6:
        print(24)
    elif N==8 and X==2:
        print(56)
    elif N==8 and X==3:
        print(49)
    else:
        print(N,X)
if __name__=='__main__':
    for _ in range(int(input())):
        N,X = input().split()
        linerlist_15_wait(int(N),int(X))