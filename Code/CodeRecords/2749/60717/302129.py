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
    tmp1.append(list1[i]-1)
    tmp1.append(i+1)
    list2.append(tmp1)
list2.sort()
print(list1)
print(str1)
print(list2)