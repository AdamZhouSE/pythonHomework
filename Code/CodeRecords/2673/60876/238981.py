import sys

t=int(sys.stdin.readline())
for i in range(0,t):
    num=int(sys.stdin.readline())
    bit=[]
    sum=0
    while num!=0:
        bit.append(num%2)
        num=num//2
    for j in range(len(bit)-1,0,-1):
        bit[j-1]=bit[j]^bit[j-1]
    for i in range(0,len(bit)):
        if bit[i]==1:
            sum+=2**i
    print(sum)