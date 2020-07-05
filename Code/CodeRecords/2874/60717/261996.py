n=int(input())
list1=input().split()
for i in range(0,n):
    list1[i]=int(list1[i])
for i in range(0,n-1):
    if list1[i]==1and list1[i+1]==3:
        list1[i+1]=2
    if list1[i]==2and list1[i+1]==3:
        list1[i+1]=1
for i in range(0,n-1):
    if list1[i]==1and list1[i+1]==1:
        list1[i+1]=0
    if list1[i]==2and list1[i+1]==2:
        list1[i+1]=0
print(list1.count(0))