list1=eval(input())
list2=eval(input())
set1=set(list1)
set2=set(list2)

result=sorted(list(set1&set2))
countList=[]

for num in result:
    if list1.count(num)>1 and list2.count(num)>1:
        times=min(list1.count(num),list2.count(num))
        for i in range(0,times-1):
            countList.append(num)

result.extend(countList)
result.sort()
print(result)