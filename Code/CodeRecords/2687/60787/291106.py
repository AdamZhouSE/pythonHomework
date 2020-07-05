t=int(input())
re=[1]
for ex in range(0,t):
    n=int(input())
    while re[-1]<=n:
        if len(re)%2==1:
            re.append(2*re[-1])
        else:
            re.append(2*re[-1]+1)
    p=[str(i) for i in re[0:len(re)-1]]
    print(" ".join(p))