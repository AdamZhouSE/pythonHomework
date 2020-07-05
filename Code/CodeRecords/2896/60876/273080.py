s1=list(input().split(" "))
s2=list(input().split(" "))
list1=[]
list2=[]
jud=True
for item in s1:
    list1.extend(list(item))
for item in s2:
    list2.extend(list(item))
for item in list2:
    if item in list1:
        index=list1.index(item)
        del list1[index]
    else:
        print("NO",end="")
        jud=False
if jud:
    print("YES",end="")