t=int(input())
for ex in range(0,t):
    n=int(input())
    num=[int(i) for i in input().split(" ")]
    re=[]
    for i in num:
        if i%2==0:
            re.append(i)
    for i in num:
        if i%2==1:
            re.append(i)
    re=[str(i) for i in re]
    print(" ".join(re))