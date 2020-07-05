strs=input().split(',')
lists = [int(i) for i in strs]
lists.sort()
check = False
for x in range(1,len(lists)):
    if (len(lists)%x==0 and x!=1) or (len(lists)==1 and x==1):
        check = True
if check:
    sets = list(set(lists))
    sets.sort()
    if len(lists)%len(sets)==0:
        check2 = True
        k = len(lists)//len(sets)
        for j in range(len(sets)):
            if lists.count(sets[j])!=k:
                check2=False
                break
        print(True) if check2 else print(False)
    else:
        print("False")
else:
    print("False")