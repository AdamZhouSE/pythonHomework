n=int(input())
for a in range(0,n):
    num=int(input())
    l=input().split(" ")
    l=list(int(a) for a in l)
    l=sorted(l)
    max=l[-1]
    while(max>0):
        count=0
        for b in range(1,max+1):
            if(num-b>=0 and l[num-b]>=max):
                count=count+1
        if(count==max):
            print(max)
            break
        else:
            max=max-1
    
        