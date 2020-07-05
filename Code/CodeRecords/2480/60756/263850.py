def divide()->list:
    N=int(input())
    arr=list(map(int,input().split()))
    odd=[]
    even=[]
    for i in arr:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    even.extend(odd)
    return even

T=int(input())
for t in range(T):
    arr=divide()
    for i in arr:
        print("%d " %(i),end="")
    print()