def solve():
    def gcd(a,b):
        while b:
            a,b=b,a%b
        return a
    def lcm(a,b):
        return a*b//gcd(a,b)

    nums=list(map(int,input().split(',')))
    for n in nums:
        for m in nums:
            if lcm(n,m)==1:
                return True

    return False

if  __name__ == '__main__' :
    if solve():
        print("True")
    else:
        print("False")