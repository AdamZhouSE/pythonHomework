def f(s):
    if s==0:
        return 0
    else:
        min=100
        for i in range(1,s+1):
            if i*i<=s:
                if f(s-i*i)+1<min:
                    min=f(s-i*i)+1
        return min
    
print(f(int(input().strip())))    
    

