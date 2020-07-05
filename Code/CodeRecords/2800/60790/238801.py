str1=input().split()
n=int(str1[0])
d=int(str1[1])
numList=input().split()
numList=list(map(int,numList))
count=0
for i in range(0,n-1):
    while(numList[i]>=numList[i+1]):
        numList[i+1]=numList[i+1]+d
        count=count+1
print(count)