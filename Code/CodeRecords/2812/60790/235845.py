num=int(input())
list1=input().split()
list1.sort()
while(list1[0]=='0'):
    del list1[0]
    num=num-1
    
mark=list1[0]
count=1
for i in range(1,num):
    if(list1[i]!=mark):
        mark=list1[i]
        count=count+1
    
print(count)