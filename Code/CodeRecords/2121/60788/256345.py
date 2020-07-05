def f(s):
    if s==1:
        return 10
    elif s==2:
        return 90
    else:
        return (10-s)*f(s-1)
    
    
print(f(int(input().strip())))   