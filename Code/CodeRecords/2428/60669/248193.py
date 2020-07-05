t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    odd=[]
    even=[]
    for item in arr:
        if item%2==0:
            even.append(item)
        else:
            odd.append(item)
    odd.sort(reverse=True)
    even.sort()
    result=odd+even
    string="".join(str(x)+" " for x in result)
    print(string)
