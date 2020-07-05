t=int(input())
def p(n):
    if(n==0 or n==1 or n==2):
        return 1
    else:
        return p(n-2)+p(n-3)
for i in range(t):
    n=int(input())
    print(p(n))