size=int(input())
list1=input().split()
list1=[int(list1[i]) for i in range(size)]
list1.sort()
count=0
for i in range(len(list1)-1):
    while list1[i]>=list1[i+1]:
        list1[i+1]+=1
        count+=1
print(count)