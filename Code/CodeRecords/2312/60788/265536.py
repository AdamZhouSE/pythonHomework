def f(s):
    if s<=1:
        return 1
    else:
        t=0 
        for i in range(s):
            t+=f(i)*f(s-1-i)
        return t%(1000000007)
            
print(f(int(input().strip())))