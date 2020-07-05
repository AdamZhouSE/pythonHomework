def gcd(a,b):
    return a if b==0 else gcd(b,a%b)
def cnt(x1,y1,x2,y2):
    return gcd(abs(x1-x2),abs(y1-y2))-1
t=int(input())
for _ in range(t):
    x1,y1=map(int,input().split())
    x2,y2=map(int,input().split())
    x3,y3=map(int,input().split())
    S=abs((x1*y2+x2*y3+x3*y1-x1*y3-x2*y1-x3*y2)/2)
    s=0
    s+=cnt(x1,y1,x2,y2)+cnt(x1,y1,x3,y3)+cnt(x2,y2,x3,y3)+3
    print(int(S-s/2+1))