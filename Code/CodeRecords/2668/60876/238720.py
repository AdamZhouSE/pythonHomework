import sys

t=int(sys.stdin.readline())
for i in range(0,t):
    num=int(sys.stdin.readline())
    temp=num
    bit=0
    sum=0
    while temp>0:
        bit+=1
        temp=temp//2
    for j in range(0,bit):
        sum+=2**j
    print(sum-num,end=" ")
    print(sum)