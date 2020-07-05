def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

num=int(input())
for i in range(num):
    first=input().split(" ")
    second=input().split(" ")
    third=input().split(" ")
    x1=int(first[0])
    y1=int(first[1])
    x2=int(second[0])
    y2=int(second[1])
    x3=int(third[0])
    y3=int(third[1])
    s=abs((x1*y2+x2*y3+x3*y1-x1*y3-y1*x2-y2*x3)/2)
    l1=gcd(abs(x1-x2),abs(y1-y2))
    l2=gcd(abs(x1-x3),abs(y1-y3))
    l3=gcd(abs(x2-x3),abs(y2-y3))

    print(int(s-(l1+l2+l3)/2)+1)