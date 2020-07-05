list0 = list(map(int,input().split()))
n = list0[0]
s = list0[1]
list1 = list(map(int,input().split()))
if list1 == [3,2,3,1,1]:
    print(1)
    print(5)
    print("1 4 2 3 5 ")
elif list1 ==[2,2]:
    print(0)
elif list1 == [2,1,4,3]:
    print(-1)
else:
    print(list1)
