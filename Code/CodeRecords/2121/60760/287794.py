n=int(input())
count=0
for i in range(pow(10,n)):
    list1=list(str(i))
    l1=len(list1)
    list2=set(list1)
    l2=len(list2)
    if l1==l2:
        count=count+1
print(count)