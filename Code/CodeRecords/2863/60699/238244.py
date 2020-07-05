list1=[int(e) for e in input().split(' ')]
list2=[int(e) for e in input().split(' ')]
res=0
for i in list2:
    if i>list1[1]:
        res+=2
    else:
        res+=1
print(res)