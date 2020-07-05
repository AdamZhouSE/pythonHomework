n=int(input())
list1=input().split()
list1=[int(x) for x in list1]
list2=input().split()
list2=[int(x) for x in list2]
a=list2[0]
b=list2[1]
if b-a==1:
    print(list1[a-1])
if b-a>1:
    sum=0
    for i in range(b-a):
        sum+=list1[a+i-1]
    print(sum)
        