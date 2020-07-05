n=int(input())
list1=input().split()
for i in range(0,n):
    list1[i]=int(list1[i])
count=0
for i in range(1,n-1):
    if (list1[i] < list1[i+1] and list1[i] < list1[i-1]) or (list1[i] > list1[i+1] and list1[i] > list1[i-1]):
        count+=1
print(count)