times=int(input())
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
for i in range(times):
    line=input().split()
    n=int(line[0])
    m=int(line[1])
    if n==1 or m==1:
        print(1)
    else:
        n=n-1
        m=m-1
        n=n+m
        print(int(factorial(n)/(factorial(m)*factorial(n-m))))