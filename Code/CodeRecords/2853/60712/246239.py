n = int(input())
list1 = list(map(int,input().split()))
oddNum=0
for i in range(n):
    if list1[i]%2!=0:
        oddNum+=1
if oddNum%2==0:
    print(len(list1)-oddNum)
else:
    print(oddNum)