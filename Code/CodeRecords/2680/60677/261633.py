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
    n=n+m
    print(factorial(n)/(factorial(m)*factorial(n-m)))