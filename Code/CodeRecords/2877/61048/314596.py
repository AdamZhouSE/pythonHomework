def arr12():
    n=int(input())
    arr=[int(x) for x in input().split(" ")]
    arr.sort()
    A,B=[],[]
    for n in arr:
        if(n<=0):
            B.append(n)
    for num in arr:
        if(num>0):
            A.append(num)
        
    sumA=sum(A)
    sumB=sum(B)
    print(sumA-sumB)
    return

arr12()