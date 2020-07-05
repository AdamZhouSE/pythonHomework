n=int(input())
res=[]
for _ in range(n):
    k=int(input())
    nums=list(map(int, input().split(" ")))
    odd=[]
    even=[]
    for h in nums:
        if h%2==0:
            even.append(h)
        else:
            odd.append(h)
    odd=sorted(odd)[::-1]
    even=sorted(even)
    nums=odd+even
    res.append(nums)
for t in res:
    for h in t:
        print(str(h)+" ",end='')
    print()