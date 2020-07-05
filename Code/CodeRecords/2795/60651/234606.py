n=int(input())
list1=input().split()
list1=[int(x) for x in list1]
set1=set(list1)
list1=list(set1)
list1.sort()
if len(list1)>3:
    print("-1")
elif len(list1)==1:
    print("0")
elif len(list1)==2:
    if (list1[1]-list1[0])%2==0:
        print (int((list1[1]-list1[0])/2))
    else:
         print(list1[1]-list1[0])
else:
    if list1[2]-list1[1]==list1[1]-list1[0]:
        print(list1[2]-list1[1])
    else:
        print("-1")
    