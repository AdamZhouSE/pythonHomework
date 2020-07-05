cnt=int(input())
list1=[]
for i in range(0,cnt):
    list2 = list(map(int, input().split(' ')))
    list1.append((list2[0],list2[1]))
list1.sort()
flag=True
for i in range(1,len(list1)):
    if list1[i][1]<list1[i-1][1]:
        flag=False
        break
if flag:
    print("Poor Alex")
else:
    print("Happy Alex")