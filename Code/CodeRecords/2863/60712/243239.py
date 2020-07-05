list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
beyond_h = 0
for i in range(len(list2)):
    if list2[i]>list1[1]:
        beyond_h = beyond_h+1
print(beyond_h+list1[0])