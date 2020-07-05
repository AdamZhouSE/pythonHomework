T=int(input())
result=[]
for i in range(0,T):
    arr=input().split(' ')
    nums,r,b=int(arr[0]),int(arr[1]),int(arr[2])
    rr=[int(n) for n in input().split(' ')]
    bb=[int(n) for n in input().split(' ')]
    sum=0
    x,y,xindex,yindex=0,0,0,0
    while nums>0:
        if r>0 and b>0:
           x=max(rr)
           xindex=rr.index(x)
           y=max(bb)
           yindex=bb.index(y)
           if x>y:
               sum=sum+x
               r=r-1
               rr[xindex]=0
               bb[xindex]=0
           elif y>x:
               sum=sum+y
               b=b-1
               rr[yindex]=0
               bb[yindex]=0
           else:
               rsum=0
               bsum=0
               for k in range(0,len(rr)):
                   rsum=rsum+rr[k]
               for k in range(0,len(bb)):
                   bsum=bsum+bb[k]
               if bsum>rsum:
                   sum=sum+x
                   r=r-1
                   rr[xindex]=0
                   bb[yindex]=0
               else:
                   sum = sum + y
                   b = b - 1
                   rr[yindex] = 0
                   bb[yindex] = 0
        elif r>0:
            x=max(rr)
            xindex=rr.index(x)
            sum = sum + x
            r = r - 1
            rr[xindex] = 0
            bb[xindex] = 0
        else:
            y=max(bb)
            yindex=bb.index(y)
            sum = sum + y
            b = b - 1
            rr[yindex] = 0
            bb[yindex] = 0
        nums=nums-1
    result.append(sum)
for i in range(0,T):
    print(result[i])