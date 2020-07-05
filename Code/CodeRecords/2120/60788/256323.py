def f(k,s):
    if s==2:
        return 1
    else:
        if k>=int(s/2):
            if s%2==0:
                return int(s*s/4)
            else:
                return int(s/2)*(int(s/2)+1)
        else:
            return max(k*f(k,s-k),f(k+1,s))

print(f(1,int(input().strip())))        