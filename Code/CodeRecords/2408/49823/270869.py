def ai(n):
    from scipy.special import perm
    num=0
    for i in range(1,n+1):
        if ai_1(i):
            num+=1
    print((int(perm(num,num))*int(perm(n-num,n-num)))%(10**9+7))
def ai_1(n):
    if n<=1:
        return False
    import math
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
if __name__ == '__main__':
    ai(int(input()))
