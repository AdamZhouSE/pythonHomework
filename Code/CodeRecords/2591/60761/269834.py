def isPrimer(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return "No"
    return "Yes"

t=int(input())
for i in range(t):
    n=int(input())
    print(isPrimer(n+2))