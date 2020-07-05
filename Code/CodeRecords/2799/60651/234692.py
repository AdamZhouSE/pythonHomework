n=int(input())
list1=input().split()
list1=[int(x) for x in list1]
list2=[]
for i in list1:
    num=i
    a=num%3
    while(a==0):
        num=int(num/3)
        a=num%3
    b=num%2
    while(b==0):
        num=int(num/2)
        b=num%2
    list2.append(num)
set1=set(list2)
if len(set1)==1:
    print("Yes")
else:
    print("No")