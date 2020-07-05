lst1 = list(map(int,input().split(',')))
lst2 = list(map(int,input().split(',')))

res = 0
for i in range(len(lst1)):
    for j in range(len(lst1)):
        res = max(res,abs(lst1[i]-lst1[j])+abs(lst2[i]-lst2[j])+abs(i-j))
print(res)