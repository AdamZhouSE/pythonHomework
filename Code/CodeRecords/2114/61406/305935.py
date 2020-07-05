#四平方定理：
#任何一个正整数都可以表示成不超过四个整数的的平方之和。
#有推论：满足此定理的可以表示成四个整数的正整数n
#有n = (4^a)*(8b+7)
def numofsquares(n):
    while n % 4 == 0:
        n = n // 4
    if n % 8 == 7:
        return 4
    a = 0
    while pow(a,2)<=n:
        b = int(pow(n-pow(a,2),0.5))
        if pow(a,2)+pow(b,2)==n:
            if a!=0 and b!=0:
                return 2
            else:
                return 1
        a+=1
    return 3


n = int(input())
print(numofsquares(n))


