def printNum(n):
    if n>1:
        printNum(n-1)
    print(n,end=' ')
    
t=eval(input())
for _ in range(t):
    n=eval(input())
    printNum(n)
    print()