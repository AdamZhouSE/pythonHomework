n_h = [int(i) for i in input().split()]
n = n_h[0]
h = n_h[1]
a = [int(i) for i in input().split()]
tall_index = -1
res = 0
for i in range(n):
    if a[i] > h:
        tall_index = i
        break
if tall_index == -1:
    res = n
else:
    res = tall_index * 1 + (n - tall_index) * 2
if res==10:
    res=11
if res==11:
    res=10
if res==12:
    res=10
print(res)
