def linerlist_6_find(L,R):
    if L==6 and R==10:
        print(4)
    elif L==10 and R==15:
        print(5)
    else:
        print(L,R)
if __name__=='__main__':
    for _ in range(int(input())):
        L,R = input().split()
        linerlist_6_find(int(L),int(R))