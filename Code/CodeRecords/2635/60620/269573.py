k=int(input())
result=0
def f(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
def num(n):
    n=f(n)
    s=str(n)
    number=0
    for i in range(len(s)):
        if(n%10==0):
            number+=1
            n//=10
    return number
for i in range(100):
    if(num(i)==k):
        result+=1
print(result)