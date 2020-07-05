size=int(input())
str1=input()
list2=str1.split()
list2=[int(list2[i]) for i in range(size)]
n=int(input())
for i in range(n):
    list1=input().split()
    s=int(list1[0])-1
    e=int(list1[1])
    count=1
    list0=[]
    for j in range(s,e):
        list0.append(list2[j])
    list0.sort()
    for j in range(len(list0)-1):
        if list0[j+1]!=list0[j]:
            count+=1
    print(count)
