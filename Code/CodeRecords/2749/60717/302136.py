n=int(input())
list1=input().split()
for i in range(0,n-1):
    list1[i]=int(list1[i])-1
str1=input()
list2=[[str1[0],0,0]]
for i in range(0,n-1):
    tmp1=[]
    tmp2=str1[i+1]
    index=list1[i]
    while index!=0:
        tmp2+=str1[index]
        index=list1[index-1]
    tmp2+=str1[0]
    tmp1.append(tmp2)
    tmp1.append(list1[i])
    tmp1.append(i+1)
    list2.append(tmp1)
list2.sort()
for i in range(0,n-1):
    for j in range(i+1,n):
        if list2[i][0]==list2[j][0] and list2[i][2]>list2[j][2]:
            list2[i],list2[j]=list2[j],list2[i]
for i in range(0,n-1):
    for j in range(i+1,n):
        if list2[i][0]==list2[j][0] and list2[i][1]>list2[j][1]:
            list2[i],list2[j]=list2[j],list2[i]