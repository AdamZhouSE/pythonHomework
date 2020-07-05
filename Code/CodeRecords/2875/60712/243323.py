n = int(input())
list2 = [0]*n
list1 = list(map(int,input().split()))
for i in range(n):
    list2[list1[i]-1]=i+1
print(*list2)
