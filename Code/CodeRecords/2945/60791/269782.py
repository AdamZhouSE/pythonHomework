s = list(input())

x = 0
boy,girl = 0,0
while(x<len(s)):
    
    if(s[x] == '.'):
        pass
    elif(s[x] == 'b'):
        boy+=1
        if(s[x+1] == 'o'):
            x+=1
            if(s[x+1] == 'y'):
                x+=1
    elif(s[x] == 'o'):
        boy+=1
        if(s[x+1]=='y'):
            x+=1
    elif(s[x] == 'y'):
        boy+=1
    elif(s[x] == 'g'):
        girl += 1
        if(s[x+1] == 'i'):
            x+=1
            if(s[x+1] == 'r'):
                x+=1
                if(s[x+1] == 'l'):
                    x+=1
    elif(s[x] == 'i'):
        girl += 1
        if(s[x+1] == 'r'):
            x+=1
            if(s[x+1] == 'l'):
                x+=1
    elif(s[x] == 'r'):
        girl+=1
        if(s[x+1]=='l'):
            x+=1    
    elif(s[x] == 'l'):
        girl+=1
    x+=1
print(boy)
print(girl,end='')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        