n=int(input())
for i in range(n):
    l=eval('['+input().replace(' ',',')+']')
    x=l[0]
    y=l[1]
    if 2*min(x//y-1,x-x//y)+1<y:
        print(0)
    else:
        print(1)