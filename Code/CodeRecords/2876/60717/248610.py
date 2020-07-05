n=int(input())
list1=input().split()
for i in range(0,n):
    list1[i]=int(list1[i])
count=0
for i in range(0,n-2):
    if list1[i]==1 and list1[i+1]==0 and list1[i+2]==1:
        list1[i+2]=0
        count+=1
print(count)