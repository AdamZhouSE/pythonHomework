t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    i=0
    while((2**i)<n):
        i=i+1
    print(2**i)