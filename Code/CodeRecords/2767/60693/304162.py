def find_ways(n):
    res=0;
    for i in range(0,n+1,3):
        for j in range(0,n+1,5):
            for k in range(0,n+1,10):
                if i+j+k==n:
                    res+=1
    return res

cases=int(input())
for i in range(cases):
    n=int(input())
    print(find_ways(n))