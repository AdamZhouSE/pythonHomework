t=int(input())
for _ in range(t):
    n=int(input())
    arr = [int(x) for x in input().split(" ")]
    num=0
    onenum=0
    twonum=0
    for i in arr:
        if i%3==0:
            num+=1
        elif i%3==1:
            onenum+=1
        else:twonum+=1
    num+=min(onenum,twonum)+abs(onenum-twonum)//3
    print(num)