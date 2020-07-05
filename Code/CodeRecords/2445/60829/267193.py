a=str(input()).split(",")
aa=[x for x in a[0][1:len(a[0])-1]]
bb=[x for x in a[1][1:len(a[1])-1]]
aa.sort()
bb.sort()
if aa==bb:
    print("True")
else:
    print("false")