num=int(input())
list=input().split(" ")
all=0
for i in range(num):
    list[i]=int(list[i])
list.sort()
sig=0
count=0
for i in range(1,num):
    if(list[i]<=list[i-1]):

        count=count+list[i-1]-list[i]+1

        list[i]=list[i-1]+1
print(count)