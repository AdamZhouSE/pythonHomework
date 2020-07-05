n = int(input())
list1 = [int(i) for i in input().split()]
start = 0
end = 0
for i in range(len(list1)-1):
    if list1[i] >= list1[i+1]:
        start = i
        break
for i in range(len(list1)-1):
    if list1[n-i-2] <= list1[n-1-i]:
        end = i
        break
m = list1[start]
res = "YES"
if start != end:
    for i in range(start,n-end):
        if list1[i] != m:
            res = "NO"
print(res)