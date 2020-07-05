length=int(input())
statistics=[]
init=[int(x) for x in input().split()]
while len(init)>0:
    key=init[0]
    statistics.append([key,init.count(key)])
    while key in init:
        init.remove(key)
countOdd=0
countEven=0
for i in statistics:
    if i[0]%2==1:
        countOdd+=i[1]
    else:
        countEven+=i[1]
print(min(countOdd,countEven))