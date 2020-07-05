def f(a):
    m=ord('A')-1
    if a<=26:
        return chr(m+a)
    else:
        return f(int(a/26))+f(a%26)
    
    
    
print(f(int(input().strip())))