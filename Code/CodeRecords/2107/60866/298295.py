def shuzi(n):
    return (n & (n-1))==0
n=int(input())
print(shuzi(n))