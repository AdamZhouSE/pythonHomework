def isT(n):
    co = 0
    for j in range(1, n+1):
        if n % j == 0:
            co += 1
            if co > 2 or n==1:
                return False
    return True
def Linerlist_8_pen(first,second):
    third = 1
    while not isT(first+second+third):
        third += 1
    print(third)
if __name__=='__main__':
    for _ in range(int(input())):
        first,second = input().split()
        Linerlist_8_pen(int(first),int(second))