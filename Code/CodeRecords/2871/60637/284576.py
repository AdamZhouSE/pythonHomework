n=(int)(input())
arr=list(map(int,input().split(' ')))
count1=0
count2=0
for i in arr:
    if(i==1):
        count1+=1
    else:
        count2+=1
print(count1 if count2>=count1 else count2+(int)((count1-count2)/3))