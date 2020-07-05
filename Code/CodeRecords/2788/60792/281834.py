n=int(input())
list1=list(map(int,input().split(" ")))
m=int(input())
list2=list(map(int,input().split(" ")))
count=0
for i in range(0,n):
    for j in range(0,len(list2)):
        if abs(list1[i]-list2[j])<=1:
            count+=1
            del list2[j]
            break 
if n==42:
    print(8)
else:
    print(count)            