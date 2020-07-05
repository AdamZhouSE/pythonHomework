All=int(input())

for q in range(0,All):
    i=int(input())

    n=0
    for k in range(0,i):
        n+=(2*k+1)*(i-k)
    print(n)