case=int(input())

for i in range(case):
    n=int(input())
    temp=[int(x) for x in input().split(' ')]
    dis=0
    for m in range(n):
        for n in range(m+1,n):
            if(temp[n]>temp[m]):
                if(temp[n]-temp[m]>dis):
                    dis=temp[n]-temp[m]
    print(dis)