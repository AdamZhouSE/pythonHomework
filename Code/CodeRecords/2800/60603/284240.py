string=input().split(" ")
num=int(string[0])
d=int(string[1])
list=input().split(" ")
for i in range(num):
    list[i]=int(list[i])
count=0
for i in range(1,num):
    if(list[i]>list[i-1]):
        continue
    else:
        while(list[i]<=list[i-1]):
            list[i]+=d
            count+=1
print(count)