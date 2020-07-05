T=int(input())
for t in range(0,T):
    R=int(input())
    S=3.14*R*R
    result=0
    for i in range(1,R):
        for j in range(i,R):
            if i*j<S:
                result=result+1
    print(result)
                