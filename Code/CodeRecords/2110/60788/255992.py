def f(s):
    while s%2==0:
        s=int(s/2)
    while s%3==0:
        s=int(s/3)
    while s%5==0:
        s=int(s/5)
        
    return s==1

print(f(int(input().strip())))