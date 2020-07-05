num=int(input())
for n in range(num):
    line=list(map(int,input().split()))
    size1=line[0]
    size2=line[1]
    lst2=list(map(int,input().split()))
    lst1 = list(map(int, input().split()))
    lst1.sort()
    lst2.sort()
    rs='No'
    no=False
    while len(lst1)!=0:
        
        removed=False
        for l in lst2:

            if l==lst1[0]:
                lst1.remove(lst1[0])
                lst2.remove(l)
                removed=True
                break
            if l>lst1[0]:
                no=True
                break
        if not removed:
            lst1.remove(lst1[0])
            no=True
        if no:
            break
    if not no:
        rs='Yes'
    print(rs)