cnt=int(input())
list1=[]
list2=[]
for i in range(0,cnt):
    list2.append(1)
list1.append(list2)
for i in range(1,cnt):
    list2=[1]
    for j in range(1,cnt):
        list2.append(0)
    list1.append(list2)
for i in range(1,cnt):
    for j in range(1,cnt):
        list1[i][j]=list1[i][j-1]+list1[i-1][j]
print(list1[cnt-1][cnt-1])