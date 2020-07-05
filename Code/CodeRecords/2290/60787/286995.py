n=int(input())
for e in range(0,n):
    l=int(input())
    num=[int(i) for i in input().split(" ")]
    re=[]
    for i in range(0,len(num)-1):
        if num[i+1]<num[i]:
            re.append(num[i+1])
        else:
            re.append(-1)
    re.append(-1)
    re=[str(i) for i in re]
    print(" ".join(re),end=" \n")