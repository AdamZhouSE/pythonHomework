N=int(input())
for n in range(0,N):
    k=int(input())
    result=0
    for i in range(k,0,-1):
        temp=int(i*(2+2*(i-1))/2)
        result=result+temp
    print(result)
