def nums_24_perfectNum(n):
    co = []
    for i in range(1, int(n/2)+1):
        if n % i == 0:
            co.append(i)
    if sum(co) == n:
        print(True)
    else:
        print(False)
if __name__=='__main__':
    n = int(input())
    nums_24_perfectNum(n)