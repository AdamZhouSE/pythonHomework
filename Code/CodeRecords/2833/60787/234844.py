n=int(input())
v=0
list1=[int(i) for i in input().split()]
list2=[int(i) for i in input().split()]
for i in list1:
    v+=i
list2=sorted(list2)
if v>list2[n-2]+list2[n-1]:
    print("NO")
else:
    print("YES")