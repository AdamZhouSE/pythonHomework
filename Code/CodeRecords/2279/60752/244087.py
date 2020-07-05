num=int(input())
for n in range(num):
    line=list(map(int,input().split(' ')))
    size=line[0]
    sum=line[1]
    lst=list(map(int,input().split(' ')))
    i=1
    rs=-1
    while i<size:
        if rs is not -1:
            break
        for length in range(1,size-i+1):
            s=0
            for e in lst[i-1:i+length]:
                s+=e
            if s==sum:
                rs=str(str(i)+' '+str(i+length))
        i+=1

    print(rs)