count=int(input())
for i in range(count):
    r=int(input())
    length =width=1
    max_square=2*r**2
    ans=0
    while (width/2)**2+(length/2)**2<=r**2:
        ans+=1
        if  ((width+1)/2)**2+(length/2)**2<=r**2:
            width+=1
        else:
            length+=1
            width=1
    print(ans)