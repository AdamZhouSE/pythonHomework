star=input().split(",")
end=input().split(",")
profit=input().split(",")
for i in range(0,len(star)):
    star[i]=int(star[i])
    end[i]=int(end[i])
    profit[i]=int(profit[i])
list1=[0 for i in range(0,max(end))]
for i in range(1,len(list1)):
    while i+1 in end:
        index=end.index(i+1)
        list1[i]=max(list1[i],list1[star[index]-1]+profit[index])
        star.pop(index)
        end.pop(index)
        profit.pop(index)
    list1[i]=max(list1[i],list1[i-1])
print(list1[len(list1)-1])    