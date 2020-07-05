n = int(input())
list1 = list(map(int,input().split()))
list1.sort()
sum = 0
for i in range(int(n/2)):
    sum =sum+ (list1[i]+list1[n-1-i])*(list1[i]+list1[n-1-i])
print(sum)