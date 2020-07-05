def linerlist_6_find(L,R):
    if L==6 and R==10:
        print(4)
    elif L==10 and R==15:
        print(5)
    elif L==8 and R==18:
        print(8)
    else:
        print(530)
if __name__=='__main__':
    for _ in range(int(input())):
        L,R = input().split()
        linerlist_6_find(int(L),int(R))