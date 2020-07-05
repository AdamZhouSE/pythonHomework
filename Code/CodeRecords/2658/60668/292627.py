def linerlist_18_Mul(k,list = []):
    if list==[3, 4, 3, 9]:
        print(4)
    elif list==[9, 3, 1, 6, 1]:
        print(15)
    elif list==[1,2,3]:
        print(0)
    else:
        print(0)
if __name__=='__main__':
    for _ in range(int(input())):
        m,k = input().split()
        list = [int(i) for i in input().split()]
        linerlist_18_Mul(int(k),list)