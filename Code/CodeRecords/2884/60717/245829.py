list1=input().split()
n=int(list1[0])
d=int(list1[1])
list2=input().split()
for i in range(0,n):
    list2[i]=int(list2[i])
count=0
for i in range(0,n):
    for j in range(0,n):
        if (i!=j) and abs(list2[i]-list2[j])<=d:
            count+=1
print(count)