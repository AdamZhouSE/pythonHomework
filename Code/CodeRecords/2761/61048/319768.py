def tb25():
    n=int(input())
    for a in range(n):
        k=int(input())
        res=0
        for i in range(1,k+1):
            res+=i**2
        print(res)
    return

tb25()