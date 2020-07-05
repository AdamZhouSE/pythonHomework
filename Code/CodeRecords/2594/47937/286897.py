n=int(input())

i=0

while i<n:
    a=input()
    start=0
    end=len(a)-1
    tiaochu=0
    
    while start<len(a):
        end=len(a)-1
        while end>start:
            if(a[start]==a[end]):
                print(end-start-1)
                tiaochu=1
                break
            end=end-1
        if(tiaochu==1):
            break
        start=start+1
    if(tiaochu==0):
        print(-1)
    i=i+1
    