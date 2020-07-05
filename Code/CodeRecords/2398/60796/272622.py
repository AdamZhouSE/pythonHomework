nums=input().split(" ")
N=int(nums[0])
T=int(nums[1])
ls=[]
for i in range(N):
    ls.append(int(input()))
for k in range(1,N+1):
    i=0
    j=i+k-1
    time=0
    subs=ls[i:j+1]
    firstTime=min(subs)
    time=time+firstTime
    subs.remove(firstTime)
    subs=[x-firstTime for x in subs]
    j=j+1
    while j<N:
        subs.append(ls[j])
        if j==N-1:
            thisTime=max(subs)
        else:
            thisTime=min(subs)
            subs.remove(thisTime)
            subs=[x-thisTime for x in subs]
        time=time+thisTime
        j=j+1
    if time<=T:
        break
print(k)

