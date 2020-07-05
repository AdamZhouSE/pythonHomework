size=int(input())
for i in range(size):
    l=int(input())
    list1=input().split()
    list0=[]
    list2=[]
    list1=[int(list1[j]) for j in range(l)]
    for j in range(l):
        if list1[j]%2==0:
            list0.append(list1[j])
        else:
            list2.append(list1[j])
    for j in range(len(list0)):
        print(list0[j],end=' ')
    for j in range(len(list2)):
        print(list2[j],end=' ')
    print()
    