n = input()
n = int(n)
list1 = input().split(" ")
list1 = [int(list1[i]) for i in range(n)]
result = 0
list2 = []
for x in list1:
    if x%2==0:
        result = result + x
    else:
        list2.append(x)
l = len(list2)
if l%2==0:
    for j in list2:
        result = result + j
else:
    for k in range(l-1):
        result = result + max(list2)
        list2.remove(max(list2))
print(result)