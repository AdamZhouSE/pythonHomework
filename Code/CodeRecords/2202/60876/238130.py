import sys

n=int(sys.stdin.readline())
def pow(n):
    sum=1
    for i in range(2,n+1):
        sum*=i
    return sum
for i in range(0,n):
    num=int(sys.stdin.readline())
    style1=num
    style2=0
    sum=0
    while style1>=0:
        sum+=pow(style1+style2)//((pow(style1))*(pow(style2)))
        style1-=2
        style2+=1
    print(sum)
