import sys

n=int(sys.stdin.readline())
def jud(n):
    sum=0
    while n!=1 and n!=4:
        while n!=0:
            sum+=(n%10)**2
            n=n//10
        n=sum
        sum=0
    if n==1:
        return True
    else:
        return False
for i in range(0,n):
    current=int(sys.stdin.readline())+1
    while True:
        if jud(current)==True:
            print (current)
            break
        else:
            current+=1
