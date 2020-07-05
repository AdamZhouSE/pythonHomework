def findLess(ele,k):
    j=0;count=0;tuple=[0,0,0]
    for i in range(len(ele)):
        j=max(j,i+1)
        while j<len(ele):
            a,b=ele[i],ele[j]
            if(a/b<=k):
                if(a/b>tuple[0]):
                    tuple[0]=a/b
                    tuple[1]=a
                    tuple[2]=b
                count+=len(ele)-j
                break
            j += 1
    return count,tuple[1],tuple[2]


b=[int(x) for x in input().lstrip("[").rstrip("]").split(",")]
a=int(input())
head=0;tail=1;middl=0.5
while True:
    middle=(head+tail)/2
    x,y,z=findLess(b,middle)
    if x==a:
        print([y,z])
        break
    elif x<a:
        head=middle
    else:
        tail=middle

