def isNotTwo(n):
    while n>1:
        if n%2==1:return True
        n=n//2
    return False

t=eval(input())
for _ in range(t):
    n=eval(input())
    if (n%2==1)&(n!=1):
        n+=1
    while isNotTwo(n):
        n+=2
    print(n)