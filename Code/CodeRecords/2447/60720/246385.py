list0=input().split()
size=int(list0[0])
n=int(list0[1])
min=size
str1=input()
list2=str1.split()
list2=[int(list2[i]) for i in range(size)]
for i in range(n):
    list1=input().split()
    s=int(list1[0])-1
    e=int(list1[1])
    min=list2[s]
    for j in range(s+1,e):
        if list2[j]<min:
            min=list2[j]
    print(min,end=' ')
