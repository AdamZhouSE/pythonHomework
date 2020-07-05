cnt=int(input())
list1 = list(map(int, input().split(' ')))
zeros=[0]
ones=[0]
zero=0
one=0

for i in list1:
    if i==1:
        one+=1
    else:
        zero+=1
    zeros.append(zero)
    ones.append(one)
res=-100000000000
for i in range(0,cnt+1):
    for j in range(i+1,cnt+1):
        res=max(res,zeros[j]-zeros[i]-(ones[j]-ones[i]))

print(res+one)