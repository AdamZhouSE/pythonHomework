size=input().split()
size1=int(size[0])
size2=int(size[1])
list1=input().split()
list2=input().split()
odd1=0
even1=0
odd2=0
even2=0
for i in range(size1):
    if int(list1[i])%2==0:
        even1+=1
    else:
        odd1+=1
for i in range(size2):
    if int(list2[i])%2==0:
        even2+=1
    else:
        odd2+=1
count=0
count=min(even1,odd2)+min(odd1,even2)
print(count)
