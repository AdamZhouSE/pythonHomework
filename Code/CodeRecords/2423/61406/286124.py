T = int(input())
for a in range(0,T):
    mn=input().split(' ')
    m = int(mn[0])
    n = int(mn[1])
    arr1 = input().split(' ')
    arr2 = input().split(' ')
    flag = True
    for i in arr2:
        if arr1.count(i)==0:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")