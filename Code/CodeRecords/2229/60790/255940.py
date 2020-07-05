list1=input().split(",")
list1=list(map(int,list1))
count1=0
count2=0
n=len(list1)
for i in range(0,n):
    for j in range(i,n):
        if(list1[i]>list1[j]):
            count1+=1
for i in range(0,n-1):
    if(list1[i]>list1[i+1]):
        count2+=1
print(count1==count2)