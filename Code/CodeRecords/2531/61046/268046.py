str = list(input())
count = {}       #dic
res = ''
for x in str:
    if x in count:
        count[x]+=1
    else:
        count[x] = 1
new_counts = sorted(count.items(), key=lambda item:item[1], reverse=True) 
#按value排序，加上reser=True从大到小排，不加从小到大排
for key,value in new_counts:
    res += value*key
print(res)