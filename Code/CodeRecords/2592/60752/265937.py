num=int(input())
for i in range(num):
    count=0
    r=int(input())
    print(r)
    for a in range(1,r-1):
        for b in range(1,r):
            if a*a+b*b<=r*r:
                count+=1
    print (count)