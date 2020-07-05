nums=int(input())
def gcd(a,b):
    if b == 0:
        return a
    else :
        return gcd(b,a%b)
    
def getDistance(p1,p2,q1,q2):
    if p1==q1:
        return abs(p2-q2)-1
    if p2==q2:
        return abs(p1-q1)-1
    return gcd(abs(p1-q1),abs(p2-q2))-1
    
for i in range(nums):
    p1,p2=input().split(' ')
    q1,q2=input().split(' ')
    r1,r2=input().split(' ')
    p1,p2,q1,q2,r1,r2=int(p1),int(p2),int(q1),int(q2),int(r1),int(r2)
    boundary=getDistance(p1,p2,q1,q2)+getDistance(p1,p2,r1,r2)+getDistance(q1,q2,r1,r2)+3
    area=abs( p1*(q2-r2) + q1*(r2-p2) + r1*(p2-q2) )
    res=(area-boundary+2)/2
    print("%.0f"%res)