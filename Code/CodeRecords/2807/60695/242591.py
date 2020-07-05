nm = input().split(" ")
n = int(nm[0])
m = int(nm[1])
l1 = input().split(" ")
l2 = input().split(" ")
odd1 = 0
odd2 = 0
even1 = 0
even2 = 0
for i in range(0, n):
    if int(l1[i]) % 2 == 1:
        odd1 += 1
    else:
        even1 += 1
for i in range(0, m):
    if int(l2[i]) % 2 == 1:
        odd2 += 1
    else:
        even2 += 1
result = min(odd1, even2) + min(odd2, even1)
print(result)