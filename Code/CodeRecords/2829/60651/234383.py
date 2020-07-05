n=int(input())
list1=input().split()
list1=[int(x) for x in list1]
list1.sort()
if len(list1)>=3:
    if list1[1]-list1[0]>=list1[len(list1)-1]-list1[len(list1)-2]:
        del(list1[0])
        print(list1[len(list1)-1]-list1[0])
    else:
        del(list1[len(list1)-1])
        print(list1[len(list1)-1]-list1[0])
else:
    print("0")