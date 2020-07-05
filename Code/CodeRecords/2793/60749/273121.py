nandc=input().split(" ")
n=int(nandc[0])
c=int(nandc[1])
timearray=list(map(int,input().split(" ")))
def count(timearray,c):
    if len(timearray)==0:
        return 0
        
    count=1
    for h in range(0,len(timearray)-1):
        if timearray[h+1]-timearray[h] <=c:
            count+=1
        else:
            count=1
    return count
print(count(timearray,c))