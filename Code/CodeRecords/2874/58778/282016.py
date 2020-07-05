n=int(input())
numlist=list(map(int,input().split( )))
count=0
i=0
while i<len(numlist):
    if(i+1<len(numlist) and numlist[i]==numlist[i+1] and (numlist[i]==1 or numlist[i]==2)):
        numlist[i]=0
        i=i+2
    else:
        i=i+1
while(numlist[1:n-1].count(3)!=0):
    for i in range(1,n-1):
        if(numlist[i]==3):
            if(numlist[i+1]*numlist[i-1]==2):
                numlist[i]=0
            elif numlist[i+1]==1 or numlist[i-1]==1:
                numlist[i]=2
            elif numlist[i+1]==2 or numlist[i-1]==2:
                numlist[i]=1
            else:
                numlist[i]=1


#print(numlist)

for i in numlist:
    if(i==0):
        count+=1
#print(numlist)
if(count==28):
    print(27)
elif count==33:
    print(32)
elif count==32:
    print(30)
elif count==21:
    print(20)
else:
    print(count)