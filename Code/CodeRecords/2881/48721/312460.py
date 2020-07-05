import math
inp = eval(input())
t = math.ceil(inp/2)



for i in range(inp):   #行数
    
    for j in range(abs(t-i-1)):
        print("*",end="")
    if(i<t):
        for k in range(abs(2*(i+1)-1)):     
            print("D",end="")
    else:
        for l in range(inp-(i-t)*2-2):
            print("D",end="")
    
    for m in range(abs(t-i-1)):
        print("*",end="")
                 
    print()