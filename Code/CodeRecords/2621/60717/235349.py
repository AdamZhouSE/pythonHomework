maxx=0

list1=eval(input())
lenn=len(list1)

for i in range(0,lenn):
    summ=0
    for j in range(i,lenn):
        summ+=list1[j]
        maxx=max(maxx,summ)
        
print(maxx)