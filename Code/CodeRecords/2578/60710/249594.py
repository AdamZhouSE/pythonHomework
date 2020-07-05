import math
def solve(num,t):
    n=num.split(",")
    n=list(map(int,n))
    x=1
    sum=0
    while True:
        for i in n:
            sum=sum+math.ceil(i/x)
        if sum<=t:
            return x
        sum=0
        x=x+1
if __name__ == '__main__':
    num=input()
    t=int(input())
    print(solve(num,t))
