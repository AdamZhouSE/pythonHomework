k=int(input())
for m in range(0,k):
    n=int(input())
    num=[int(i) for i in input().split()]
    num=sorted(num)
    re=[]
    for i in range(0,n):
        if i%2==0:
            re.append(num.pop())
        else:
            re.append(num[0])
            del num[0]
    re=[str(i) for i in re]
    print(" ".join(re))