list1=input().split()
n=int(list1[0])
time=int(list1[1])
list2=input().split()
list2=[int(x) for x in list2]
list2.sort()
sum=0
for i in range(n):
    t=time-i
    if t>1:
        sum+=t*list2[i]
    else:
        sum+=list2[i]
print(sum)
