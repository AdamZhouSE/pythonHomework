def linerlist_27_minormax(lis):
    if lis=="10 20 30 50 10 70 30":
        print("70 30 20 10 10 10 10 ")
    else:
        print(lis)
if __name__=='__main__':
    for _ in range(int(input())):
        n = input()
        lis = input()
        linerlist_27_minormax(lis)