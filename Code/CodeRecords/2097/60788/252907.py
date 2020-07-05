def f(a,b):
    if a==0:
        return '0'
    if a==b:
        return '1'
    elif a>b:
        return str(int(a/b))+f(a%b,b)[1:]
    else:
        s=[]
        while True:
            if (10*a)%b==0:
                s.append(int((a*10)/b))
                break
            else:
                s.append(int((a*10)/b))
                a=(10*a)%b
                if s[len(s)-1]==s[0]:
                    
                    return '0.'+'('+''.join([str(x) for x in s])+')'
                
        return '0.'+''.join([str(x) for x in s])
    
    
    

print(f(int(input().strip()),int(input().strip())))                    
            
            
        