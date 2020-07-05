list1=list(map(int,input().split(",")))
mid=len(list1)//2
list1.sort()
midnum=list1[mid]
sum=0
for i in range(0,len(list1)):
    sum=sum+abs(list1[i]-midnum)
print(sum)