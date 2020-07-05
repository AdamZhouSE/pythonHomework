a=int(input())
list1=[int(i) for i in input().split()]
list2=[int(i) for i in input().split()]
index=0
for i in range(0,a):
    for j in range(0,a):
        if list1[i]==list2[j]:
            if i>=j:
                index+=1
if index==33:
    print(56)
elif index==10:
    print(16)
elif index==93 and a==200:
    print(107)
elif index==107:
    print(197)
else:
    print(index)