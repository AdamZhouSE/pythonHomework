def howcanAwon(n):
    if(n%5==0):
        return "-1"
    else:
        return(n%5)
t=int(input())
for i in range(t):
    n=int(input())
    print(howcanAwon(n))
    