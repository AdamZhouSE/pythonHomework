tests = int(input())
for i in range(0,tests):
    ls = list(map(int,input().split()))
    hou = ls[0]
    mon = ls[1]
    if hou%2==1:
        print(mon*int(hou/2+1))
    else:
        print(mon*int(hou/2))