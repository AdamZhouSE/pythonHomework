list1=(input().split(','))
for i in range(0,len(list1)):
    list1[i]=int(list1[i])
list1.sort(reverse=True)
n=int(input())
print(list1[n-1])