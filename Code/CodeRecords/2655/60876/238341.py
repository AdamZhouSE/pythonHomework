import sys

t=int(sys.stdin.readline())
def jud(n):
    while(n!=0):
        if n%2==1 and n!=1:
            return False
        n=n//2
    return True
for i in range(0,t):
    num=int(sys.stdin.readline())
    while jud(num)==False:
        num+=1
    print(num)
