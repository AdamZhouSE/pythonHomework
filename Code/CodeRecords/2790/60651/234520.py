n1=int(input())
n1=int(input())
list1=input().split()
list1=[int(x) for x in list1]
list2=input().split()
list2=[int(x) for x in list2]
list3=[]
for i in list2:
    sum=0
    for j in list1:
        if j<=i:
            sum+=1
    list3.append(str(sum))
print(" ".join(list3))