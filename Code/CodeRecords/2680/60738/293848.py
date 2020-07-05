n=int(input())
def factorial(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res
for i in range(n):
    num=input()
    a=int(num[0])-1
    b=int(num[2])-1
    print(int(factorial(a+b)/(factorial(a)*factorial(b))))
    