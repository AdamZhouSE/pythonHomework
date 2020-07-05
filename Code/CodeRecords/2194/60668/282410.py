def isT(n):
    co = 0
    for j in range(1, n+1):
        if n % j == 0:
            co += 1
            if co > 2 or n==1:
                return False
    return True


def linerlist_5_find(m,n):
    re = []
    for i in range(m,n+1):
        if  isT(i):
            re.append(i)
    for i in range(len(re)-1):
        print(re[i],end=' ')
    print(re[len(re)-1],end='\n')


if __name__=='__main__':
    for _ in range(int(input())):
        m,n = input().split()
        linerlist_5_find(int(m),int(n))