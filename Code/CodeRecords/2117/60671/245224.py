list1=[]
num=int(input())
for x in range(num):
    list1.append(0)
for gap in range(1,num+1):
    time=num//gap
    for j in range(1,time+1):
        list1[j*gap-1]=1-(list1[j*gap-1])
count=0
for x in list1:
    if(x==1):
        count+=1
print(count)