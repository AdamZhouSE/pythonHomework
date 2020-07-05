N=int(input())
for n in range(0,N):
    a=int(input())
    b=str(bin(a)).replace("Ob","")
    result=0
    for item in b:
        if item=='1':
            result=result+1
    print(result)