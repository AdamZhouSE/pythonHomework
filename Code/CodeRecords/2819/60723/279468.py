num=int(input())
temp=input().split()
count1=0
count2=0
count3=0
count4=0
for i in range(num):
    if temp[i]=='1':
        count1=count1+1
    elif temp[i]=='2':
        count2=count2+1
    elif temp[i]=='3':
        count3=count3+1
    else:
        count4=count4+1
result=count4+count3+int(count2/2)
count1=count1-count3
count2=count2%2
if count1<count2*2:
    result=result+count2
else:
    count1=count1-2*count2
    result=result+count2+int((count1+3)/4)
print(result)