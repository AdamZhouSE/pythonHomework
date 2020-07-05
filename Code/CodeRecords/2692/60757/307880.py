arr=eval(input())
day=int(input())
t=max(arr)-1
d=-1
while(d<0):
    t+=1
    ind=0
    d=day
    while(ind!=len(arr)):
        tmp=t
        while(tmp>0 and ind!=len(arr)):
            if tmp-arr[ind]>=0:
                tmp=tmp-arr[ind]
                ind+=1
            else:
                break
        d-=1
print(t)    
        
    