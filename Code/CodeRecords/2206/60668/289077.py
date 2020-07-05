def f(n):
    if n==1:
        return 1
    else:
        return f(n-1)+n
def linerlist_12_F(n):
    if n==1:
        return 1
    else:
        co = 0
        re = 1
        for i in range(1,n):
            if f(i)<n:
                co = i
        for i in range(f(co)+1,n+1):
            re *= i
        return linerlist_12_F(f(co))+re
if __name__=='__main__':
    for _ in range(int(input())):
        n = input()
        print(linerlist_12_F(linerlist_12_F(int(n))))