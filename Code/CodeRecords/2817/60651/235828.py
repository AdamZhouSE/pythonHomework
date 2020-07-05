n=int(input())
list1=input().split()
list1=[int(x) for x in list1]
flag=0
for i in range(n):
    if i!=list1[i] and list1[list1[list1[i]-1]-1]==i+1:
        print("YES")
        flag=1
        break
if  flag==0:
    print("NO")
        