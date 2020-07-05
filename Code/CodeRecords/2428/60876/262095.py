N=int(input())
for i in range(0,N):
    length=int(input())
    nums=list(map(int,input().split(" ")))
    odd=[]
    even=[]
    for item in nums:
        if item%2==0:
            even.append(item)
        else:
            odd.append(item)
    odd.sort(reverse=True)
    even.sort()
    odd.extend(even)
    for j in range(0,length):
        print(odd[j],end=" ")
    print()