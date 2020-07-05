strs=input().split(',')
lists = [int(i) for i in strs]
lists.sort()
check = False
for x in range(1,len(lists)):
    if (len(lists)%x==0 and x!=1) or (len(lists)<=2 and x==1):
        check = True
if check:
    sets = list(set(lists))
    sets.sort()
    if len(lists)%len(sets)==0:
        check2 = False
        k = len(lists)//len(sets)
        for t in range(2,k+1):
            check3 = True
            for j in range(len(sets)):
                if lists.count(sets[j])!=t and lists.count(sets[j])%t!=0:
                    check3=False
                    break
            if check3:
                check2=True
                break
            else:
                continue                    
        print(True) if check2 else print("3False")
    else:
        print("2False")
else:
    print("1False")