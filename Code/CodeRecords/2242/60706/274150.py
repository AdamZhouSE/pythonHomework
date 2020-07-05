list1=input().split(',')
rec1=[]
for i in range(len(list1)):
    rec1.append(int(list1[i]))
list2=input().split(',')
rec2=[]
for i in range(len(list2)):
    rec2.append(int(list2[i]))
ans=not (rec1[2] <= rec2[0] or  rec1[3] <= rec2[1] or  rec1[0] >= rec2[2] or rec1[1] >= rec2[3])
print(ans)