def countMinReversals(expr):  
    lenn = len(expr)   
    if (lenn % 2) : 
        return -1
    s = []  
    for i in range(lenn): 
        if (expr[i] =='}' and len(s)):  
            if (s[0] == '{') : 
                s.pop(0)  
            else: 
                s.insert(0, expr[i])  
        else: 
            s.insert(0, expr[i]) 
    red_len = len(s)  
    n = 0
    while (len(s)and s[0] == '{') : 
            s.pop(0)  
            n += 1
    return (red_len // 2 + n % 2)  
  

if __name__ == '__main__':  
    t = int(input())
    while t:
        expr = input()
        print(countMinReversals(expr.strip()))
        t -= 1
        