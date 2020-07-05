t=int(input())
for i in range(t):
    n=int(input())
    threenum=n//3
    fivenum=n//5
    sum=0
    for j in range(threenum+1):
        for k in range(fivenum+1):
            if 3*j+5*k==n:
                sum=sum+1+k//2
    print(sum)