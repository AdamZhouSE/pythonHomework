import sys

t=int(sys.stdin.readline())
def jud(n):
    bit=False
    while n!=0:
        if bit==True and n%2==1:
            return True
        elif n%2==1:
            bit=True
        else:
            bit=False
        n=n//2
for i in range(0,t):
    num=int(sys.stdin.readline())
    sum=0
    for j in range(3,2**num):
        if jud(j)==True:
            sum+=1
    print(sum)