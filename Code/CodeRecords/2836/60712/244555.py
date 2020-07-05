import copy
n = int(input())
list1 =input().split()
list2 = copy.deepcopy(list1)
list2.sort()
list2 = "".join(list2)
list1 = "".join(list1)
bl = False
if list1==list2:
    print(0)
else:    
    for i in range(len(list1)):
        list1 = list1[n-1:n]+list1[0:n-1]
        if list2 ==list1:
            print(i+1)
            bl =True
            break
    if bl==False:
        print(-1)





