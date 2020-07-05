T=int(input())
temp=[]
mid=[]
for a in range(T):
    result = []
    n=int(input())
    temp.append(n)
    for i in range(2,n+1):
        while(n%i==0):
            result.append(i)
            n/=i
    if(len(result)==3):
        if (len(set(result))==3):
            mid.append(1)
        else:
            mid.append(0)
    else:
        mid.append(0)
for i in mid:
    print(i)