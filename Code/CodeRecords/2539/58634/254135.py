a = [int(i) for i in input().replace("[","").replace("]","").replace(",","").split(" ")]
b = a.copy()
n = len(a)
b.sort()
i, j = 0, n-1
while i < n and a[i] == b[i]:
    i += 1
while j>i+1 and a[j] == b[j]:
    j -= 1
print(j-i+1)
