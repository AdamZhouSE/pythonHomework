t=eval(input())
for _ in range(t):
    n=eval(input())
    arr=list(map(int,input().strip().split(' ')))
    odd=[]
    even=[]
    for i in arr:
        if i%2==1:
            odd.append(i)
        else:
            even.append(i)
    odd=sorted(odd,reverse=True)
    even=sorted(even)
    res=odd+even
    for i in range(n):
        print(res[i],end=' ')
    print()