import sys

t=int(sys.stdin.readline())
for i in range(0,t):
    num=int(sys.stdin.readline())
    bin=[]
    for j in range(0,32):
        bin.append(num%2)
        num=num//2
    num=0
    for j in range(0,16):
        num+=bin[2*j+1]*(2**(2*j))
        num+=bin[2*j]*(2**(2*j+1))
    print(num)