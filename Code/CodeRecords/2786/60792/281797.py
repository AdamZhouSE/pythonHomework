n=int(input())
list1=list(map(int,input().split(" ")))
list1.sort()
count=0
j=0
for i in range(1,n+1):
    while j<len(list1) and list1[j]<i:
        j+=1
    if j<len(list1) and list1[j]>=i:
        count+=1
        j+=1
print(count)