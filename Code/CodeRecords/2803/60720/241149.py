list1=input().split()
n=int(list1[0])
m=int(list1[1])
isR=True
list2=[0]*m
for i in range(n):
    list3=input().split()
    for j in range(int(list3[0])):
        list2[int(list3[j+1])-1]=1
for i in range(m):
    if list2[i]==0:
        print('NO')
        isR=False
        break
if isR:
    print('YES')