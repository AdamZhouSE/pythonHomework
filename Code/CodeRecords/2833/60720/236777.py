size=int(input())
list1=input().split()
list2=input().split()
count=0
for i in range(size):
    list1[i]=int(list1[i])
    count+=list1[i]
    list2[i]=int(list2[i])
list2.sort(reverse=True)
if count<=list2[0]+list2[1]:
    print('YES')
else:
    print('NO')