n=int(input())
list1=list(map(int,input().split()))
list1.sort()
count=0
for i in range(0,len(list1)):
    count=count+abs(list1[i]-i-1)
print(count)    