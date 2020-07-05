a = input()
b = input()

dic_a = {}
dic_b = {}
ans = 0
len_a = len(a)
len_b = len(b)
for i in range(0, len_a):
    for j in range(i + 1, len_a + 1):
        temp = a[i:j]
        if temp in dic_a:
            dic_a[temp] += 1
        else:
            dic_a[temp] = 1

for i in range(0, len_b):
    for j in range(i + 1, len_b + 1):
        temp = b[i:j]
        if temp in dic_b:
            dic_b[temp] += 1
        else:
            dic_b[temp] = 1

for (k,v) in dic_a.items():
    if k in dic_b:
        ans+=v*dic_b[k]
print(ans,end='')
