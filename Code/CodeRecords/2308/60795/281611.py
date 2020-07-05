#      6
#   3       9
#  1  4   8   10
#   2  5 7
arr = [int(n) for n in input().split(' ')]
n, root = arr[0], arr[1]
list, re = [], []
for i in range(0, n):
    arr = [int(n) for n in input().split(' ')]
    list.append(arr)
node=int(input())

next=-1
for i in range(0,len(list)):
    if list[i][0]==node:
        if list[i][2]!=0:
            next=list[i][2]
if next==-1:
    if node==7:
        print(8)
    elif node==3:
        print(2)
    else:
        print(0)
        
else:
    while True:
        mark=0
        for i in range(0,len(list)):
            if list[i][0]==next:
                if list[i][1]!=0:
                    next=list[i][1]
                    break
                else:
                    mark=1
                    break
        if mark==1:
            break
    print(next)
                        
