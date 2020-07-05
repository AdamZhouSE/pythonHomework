t=int(input())

for i in range(t):
    stan=[1,2,2,3]
    now=4
    x=int(input())
    while(len(stan)<x):
        for i in range(now):
            stan.append(stan[i]+1)
        now*=2
    print(stan[x]-1)
        