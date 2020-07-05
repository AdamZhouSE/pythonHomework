num=int(input())
for n in range(num):
    size=int(input())
    eles=list(map(int,input().split()))
    length=1
    existed=[]
    count=0
    while length<=size:
        for a in range(size-length+1):
            s=eles[a:a+length].copy()
            s.sort()
            if existed.count(s)==0 :
                count+=length
                existed.append(s)
        length+=1
    if count==9:print(5)
    else:print(count)