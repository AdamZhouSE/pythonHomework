num=int(input())
for n in range(num):
    size=int(input())
    eles=list(map(int,input().split()))
    length=1
    existed=[]
    count=0
    while length<size:
        for a in range(size-length):
            if existed.count(eles[a:a+length])==0:
                count+=length
                existed.append(eles[a:a+length])
        length+=1
    print(count)