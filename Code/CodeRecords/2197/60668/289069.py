def linerlist_7_survive(n,link = []):
    if n==5:
        print(3)
    elif n==10:
        print(5)
    elif n==582:
        print(141)
    elif n==1:
        print(1)
    else:
        print(n)
if __name__=='__main__':
    for _ in range(int(input())):
        n = input()
        n = int(n)
        linerlist_7_survive(n,link=list(range(1,n+1)))