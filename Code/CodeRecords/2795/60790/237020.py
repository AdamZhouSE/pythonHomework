n = int(input())
list1 = input().split()
list1 = list(map(int, list1))
list1.sort()
set1 = set(list1)
list2 = list(set1)
list2.sort()
if (len(set1) == 1):
    print(0)
elif (len(set1) == 2):
    if((list2[1]-list2[0])%2==0):
        print(int((list2[1]-list2[0])/2))
    else:
        print(list2[1]-list2[0])
elif ((len(set1) == 3) and ((list1[-1] - list1[0]) % 2 == 0) and ((list2[-1]-int((list1[-1] - list1[0]) / 2)==list2[1]))):
    print(int((list1[-1] - list1[0]) / 2))
else:
    print(-1)
