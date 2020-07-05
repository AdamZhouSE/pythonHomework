number=int(input())
count=1
list=input().split()
list.sort()
for i in range(number-1):
    if(int(list[i])!=int(list[i+1])):
        count=count+1
if(int(list[0])==0):
    count=count-1;
print(count)