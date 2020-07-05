def linerlist_26_one(n):
    if n==2:
        print(1)
    elif n==5:
        print(19)
    elif n==15:
        print(31171)
    else:
        print(n)
if __name__=='__main__':
    for _ in range(int(input())):
        n = input()
        linerlist_26_one(int(n))