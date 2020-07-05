n=int(input())
list1=input().split()
list1=list(map(int,list1))
list2=input().split()
list2=list(map(int,list2))
sum1=0
for num in range (list2[0],list2[1]):
    sum1=sum1+list1[num-1]
print(sum1)