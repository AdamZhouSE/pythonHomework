size=int(input())
list1=input().split()
list1=[int(list1[i]) for i in range(size)]
list1.sort()
count=0
base=0
for i in range(size):
    if list1[i]>=base:
        count+=1
        base+=list1[i]
print(count)