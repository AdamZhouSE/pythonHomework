T=int(input())
for t in range(0,T):
    R=int(input())
    S=2*R*R
    result=0
    for i in range(1,R*2):
        for j in range(1,R*2):
            if i*j<S:
                result=result+1
    print(result)
