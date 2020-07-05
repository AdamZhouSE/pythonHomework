num=int(input())
for i in range(num):
    size=int(input())
    eles1=list(map(int,input().split(' ')))
    eles2 = list(map(int, input().split(' ')))
    rs=0
    eles1.sort()
    eles2.sort()
    if eles1==eles2:
        rs=1
    print(rs)
        

