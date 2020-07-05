num=int(input())
list=input().split(" ")
for i in range(num):
    list[i]=int(list[i])
count=1
ans=1
for i in range(num-1):
    if(list[i]<list[i+1]):
        count+=1
    else:
        if(count>ans):
            ans=count
        count=1
if(count>ans):
    ans=count
print(ans)