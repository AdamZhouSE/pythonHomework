def isMulTwo(n):
    if n==1:
        return True
    while n>=2:
        if n==2:
            return True
        elif n%2==1:
            return False
        n=int(n/2)
    return False
t=int(input())
for i in range(t):
    n=int(input())
    while True:
        if isMulTwo(n):
            print(n)
            break
        else:
            n+=1
