n = int(input())
list1=input().split()
list2=input().split()
list3=[]
count=0
for i in range(0,len(list1)):
    list3.append(list1.index(list2[i]))
for i in range(0,n-1):
    if list3[i]>min(list3[i+1:n]):
        count+=1
print(count)