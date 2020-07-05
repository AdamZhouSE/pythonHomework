a=int(input())
list=[]
for i in range(0,a):
    a=input().split(' ')
    list.append(a)
a=int(input())
for i in range(0,a):
    list1=[]
    a=input()
    for j in range(0,len(list)):
        if a in list[j]:
            list1.append(j+1)
    print(" ".join(str(i) for i in list1),end=" ")
    print()