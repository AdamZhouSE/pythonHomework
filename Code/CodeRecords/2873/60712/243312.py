list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
list3 = list(map(int,input().split()))
result=""
for i in range(len(list2)):
    for j in range(len(list3)):
        if list2[i] == list3[j]:
            result=result +str(list2[i])
            break
print(result)