a = eval(input())
res = []
for i in range(len(a)-1):
    num = 0
    for j in range(i+1,len(a)):
        if a[j]<a[i]:
            num += 1
    res.append(num)
res.append(0)
print(res)