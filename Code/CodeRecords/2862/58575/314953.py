n=int(input())
nums=list(map(int,input().split(" ")))
nums.sort()
nums.reverse()
Odd=[]
Even=[]

for i in nums:
    if i%2==0:
        Even.append(i)
    else:
        Odd.append(i)

x=len(Odd)-len(Even)
if(x>1):
    Odd.reverse()
    sum=0
    i=0
    while(i<x-1):
        sum+=Odd[i]
        i+=1
    print(sum)
elif(x<-1):
    x=-x
    Even.reverse()
    sum=0
    i=0
    while(i<x-1):
        sum+=Even[i]
        i+=1
    print(sum)
else:
    print(0)