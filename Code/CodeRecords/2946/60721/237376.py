list=list(input())
count=0
for i in range(1,len(list)):
    if(list[i-1]!=list[i]):
        count+=1
if(list[len(list)-1]=='0'):
    count+=1
print(count,end="")