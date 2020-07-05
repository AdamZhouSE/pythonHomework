page=int(input())
indexset=list(map(int,input().split()))
daynum=0
needPage=1
for i in range(page):
    if(indexset[i]>needPage):
        needPage=indexset[i]
    if(i+1>=needPage):
        daynum+=1
print(daynum)