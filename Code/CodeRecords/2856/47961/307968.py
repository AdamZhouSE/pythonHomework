a=int(input())
list1=[]
list2=[]
for i in range(0,a):
    b=[int(i) for i in input().split()]
    list1.append(b[0])
    list2.append(b[1])
shu=2
for i in range(1,a-1):
    if abs(list1[i-1]-list1[i])>list2[i] or abs(list1[i]-list1[i+1])>list2[i]:
        shu+=1
if shu==11:
    print(10)
else:
    print(shu)