def shuzi(n):
    i=1
    while n>0:
        n=n-i
        i=i+2
    return n==0
a=int(input())
print(shuzi(a))