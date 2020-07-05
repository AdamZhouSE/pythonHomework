cnt=int(input())
list1 = list(map(int, input().split(' ')))
list1.sort()
res=0
for i in range(1,len(list1),2):
    res+=(list1[i]-list1[i-1])
print(res)