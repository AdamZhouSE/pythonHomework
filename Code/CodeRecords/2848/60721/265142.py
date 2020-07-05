a=input()
m,n=map(int,input().split(" "))
list1=input().split(" ")
list2=input().split(" ")
list1=[int(i) for i in list1]
list2=[int(i) for i in list2]
list3=[]
list4=[]
for i in range(0,m):
    list3.append(min(list1))
    list1.remove(min(list1))
for i in range(0,n):
    list4.append(max(list2))
    list2.remove(max(list2))
if(max(list3)<min(list4)):
    print("YES")
else:
    print("NO")