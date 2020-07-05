def ans(n):
    if(n==0 or n==1):
        return 1
    else:
        sum = 0
        for i in range(0,n):
            sum = sum + ans(i)*ans(n-i-1)
        return sum

for i in range(int(input())):
    n = int(input())
    res = ans(n//2)
    print(res)