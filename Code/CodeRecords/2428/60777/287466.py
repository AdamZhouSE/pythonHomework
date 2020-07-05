case=int(input())
for i in range(case):
    n=int(input())
    temp=[int(x) for x in input().split(' ')]
    odd=[]
    even=[]
    for x in temp:
        if(x%2==0):
            even.append(x)
        else:
            odd.append(x)
    odd.sort(reverse=True)
    even.sort()
    res=odd+even
    for j in range(len(res)):
        if(j!=len(res)-1):
            print(res[j],end=' ')
        else:
            print(res[j],end=' ')
    print()