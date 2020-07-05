s1, s2 = input().split()
n = int(s1)
k = int(s2)
elements = input().split()
res = 100
for element in elements:
    if k % int(element) == 0:
        res = int(min(res, k / int(element)))
print(res)