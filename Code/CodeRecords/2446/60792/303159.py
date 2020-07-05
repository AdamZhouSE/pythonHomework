num=int(input())
list2=[]
for i in range(0,num):
    list1=list(input().split())
    list2.append(list1[1:])
n=int(input())
for j in range(0,n):
    s=input()
    list3=[]
    for k in range(0,len(list2)):
        if s in list2[k]:
            list3.append(k+1)
    if list3==[]:
        print(" ")
    else:
        for i in range(0,len(list3)):
            print(list3[i],end=" ")
        print()
  