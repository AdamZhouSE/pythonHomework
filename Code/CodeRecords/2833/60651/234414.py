n=int(input())
list1=input().split()
list1=[int(x) for x in list1]
sum=0
for i in list1:
    sum+=i
list2=input().split()
list2=[int(x) for x in list2]
list2.sort(reverse=True)
ca=list2[0]+list2[1]
if(ca>=sum):
    print("YES")
else:
    print("NO")