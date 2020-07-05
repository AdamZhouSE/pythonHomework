N=int(input())
for n in range(0,N):
    K=int(input())
    result=0
    for i in range(K,0,-1):
        temp=0
        for j in range(i,0,-1):
            temp=temp+j
        result=result+temp
    print(result)