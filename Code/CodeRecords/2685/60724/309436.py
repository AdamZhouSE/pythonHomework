T=int(input())
for k in range(T):
    N=int(input())
    result=""
    for i in range(N):
        result+="0"
    while N>=10:
        result="9"+result
        N-=9
    result=str(N)+result
    print(result)