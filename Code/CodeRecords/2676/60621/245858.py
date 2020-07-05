a=eval(input())
for i in range(a):
    b=[int(x) for x in input().split()]
    c=[int(x) for x in input().split()]
    start=0
    end=start+min(b[0],b[1])-1
    now=0
    maximum=0
    i=0
    while i<=end:
        now+=c[i]
        i+=1
    maximum=now
    while end<b[0]:
        start+=1
        end+=1
        if end<b[0]:
            now=now-c[start-1]+c[end]
        maximum=max(maximum,now)
    print(maximum)