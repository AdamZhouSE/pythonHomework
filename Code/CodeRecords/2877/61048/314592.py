def arr12():
    n=int(input())
    arr=[int(x) for x in input().split(" ")]
    arr.sort()
    A,B=[],[]
    for n in arr:
        if(n<=0):
            B.append(n)
            arr.remove(n)
    if(len(B)==0):
        B.append(arr[0])
        arr.remove(arr[0])
    for num in arr:
        A.append(num)
    sumA=sum(A)
    sumB=sum(B)
    print(sumA-sumB)
    return

arr12()