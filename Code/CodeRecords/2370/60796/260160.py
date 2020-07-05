n=int(input())
re=""

while n!=0:
    if n%2==0:
        yu=0
    else:
        yu=1
    re=str(yu)+re
    n = (n - int(yu)) / -2
print(re)
