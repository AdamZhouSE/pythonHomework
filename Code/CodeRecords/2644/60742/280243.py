a = eval(input())
k = int(input())
res = -1
for i in range(1,len(a)+1):
    for j in range(len(a)-i+1):
        tmp = sum(a[j:j+i])
        if tmp>=k:
            res = i
            break
print(res)