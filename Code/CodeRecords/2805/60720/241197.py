size=int(input())
list1=input().split()
max=1
count=1
for i in range(size-1):
    if int(list1[i+1])>int(list1[i]):
        count+=1
    else:
        if count>max:
            max=count
        count=1
if(count>max):
    max=count
print(max)