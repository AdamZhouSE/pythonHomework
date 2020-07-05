num=int(input())
test=input().split()
test=list(map(int,test))
maxTime=0
count1=0
flag=0
count2=0
for i in range(1,num):
    if i!=1 and test[i]!=test[i-1]:
        flag+=1
    if flag==2:
        maxTime=max(maxTime,min(count1,count2)*2)
        if test[i-1]==1:
            count2=0
        else:
            count1=0
        flag=1
    if test[i]==1:
        count1+=1
    else:
        count2+=1

print(max(maxTime,min(count1,count2)*2))