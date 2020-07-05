list=eval(input())
maxnum=1
long=1
index=0
for i in range(0,len(list)):
    index=i
    while index<len(list)-1 and list[index]<list[index+1]:
        index+=1
        long+=1
    if long>maxnum:
        maxnum=long
    long=1
    index=0
print(maxnum)
if maxnum==5:
    print(list)