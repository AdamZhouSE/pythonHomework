num=int(input())
list=input().split(" ")
for i in range(num):
    list[i]=int(list[i])
list.sort()
count=1
index=1
while(True):
    if(index>=len(list)):
        break
    stan=list[index]
    all=0
    for i in range(index):
        all+=list[i]
    if(all<=stan):
        count+=1
        index+=1
    else:
        del(list[index])
print(count)