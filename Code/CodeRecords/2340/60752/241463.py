num=int(input())
for i in range(num):
    size=int(input())
    eles=list(map(int,input().split(' ')))
    count=0
    start=0
    end=size-1
    while end-start>1:
        a=eles[start]
        b=eles[end]
        height=min(a,b)
        for j in range(start,end):
            if eles[j]<height:

                count=count+height-eles[j]
                eles[j] = height
        if a>=b:
            end=end-1
        if a<=b:
            start=start+1


    print(count)