t=int(input())
for i in range(t):
    inlist=input().split()
    l1=inlist[0]
    l2=inlist[1]
    list1=input().split()
    list2=input().split()
    set1=set()
    for i in list1:
        for j in list2:
            if i==j:
                set1.add(i)
    print(len(set1))            