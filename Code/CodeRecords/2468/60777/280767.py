case=int(input())
for i in range(case):
    num=int(input())
    res=[int(x) for x in input().split(' ')]
    out=[]
    for j in range(num):
        su=1
        for k in range(num):
            if(k!=j):
                su*=res[k]
        out.append(su)
    for j in range(num):
        print(out[j],end=' ')
    print()
            
            