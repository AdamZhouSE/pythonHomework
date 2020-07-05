a=int(input())
for i in range(a):
    b=int(input())
    index=0
    max=0
    
    for j in range(100):
        for k in range(100):
            for l in range(100):
                if b==3*j+5*k+10*l:
                    index+=1
                    
    print(index)