n=int(input())
for i in range(0,n):
    x=int(input())
    count=0
    for j in range(0,100):
        if x<10*j:
            break
        for k in range(0,100):
            if x<5*k+10*j:
                break
            for l in range(0,100):
                if x==3*l+5*k+10*j:
                    count+=1
                elif x<3*l+5*k+10*j:
                    break
    print(count)