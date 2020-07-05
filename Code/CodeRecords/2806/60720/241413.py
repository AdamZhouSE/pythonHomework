size=int(input())
list1=[[]for i in range(size)]
for i in range(size):
    list1[i]=input().split()
base=int(list1[0][1])
count=int(list1[0][0])
sum=0
for i in range(0,size-1):
    if(int(list1[i+1][1])>base):
        count+=int(list1[i+1][0])
    else:
        sum+=count*base
        base=int(list1[i+1][1])
        count=int(list1[i+1][0])


sum+=count*base
print(sum)
