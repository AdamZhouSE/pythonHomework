n = int(input())
rectangle = []
for i in range(n):
    lst = list(map(int,input().split()))
    if lst[0]>lst[1]:
        lst[0],lst[1] = lst[1],lst[0]
    rectangle.append(lst)

flag = True
for i in range(1,len(rectangle)):
    if rectangle[i][1] > rectangle[i-1][1]:
        if rectangle[i][0]<=rectangle[i-1][1]:
            rectangle[i][0],rectangle[i][1] = rectangle[i][1],rectangle[i][0]
        else:
            flag = False
            break

if flag:
    print('YES')
else:
    print('NO')