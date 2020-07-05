list1=input().split()
list1=[int(x) for x in list1]
n=list1[0]
m=list1[1]
light=[t for t in range(1,m+1)]
for i in range(n):
    list2=input().split()
    list2=[int(x) for x in list2]
    ki=list2[0]
    del(list2[0])
    for j in list2:
        if j in light:
            light.remove(j)
if len(light)==0:
    print("YES")
else:
    print("NO")
