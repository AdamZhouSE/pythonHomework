list1=[int(e) for e in input().split(' ')]
list2=[int(e) for e in input().split(' ')]
list3=[int(e) for e in input().split(' ')]
list4=[int(e) for e in input().split(' ')]
list5=[int(e) for e in input().split(' ')]
for i in list2:
    list1.append(i)
for i in list3:
    list1.append(i)
for i in list4:
    list1.append(i)
for i in list5:
    list1.append(i)
res=0
while res<25:
    if list1[res]==1:
        break
    else:
        res+=1
line=res//5+1
res-=res//5*5
ans=abs(3-line)+abs(2-res)
print(ans)