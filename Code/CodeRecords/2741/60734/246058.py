import re
lst = re.findall(r'\d+',input())
lst = list(map(int,lst))
max_count = 1
count = 1
for i in range(0,len(lst)-1):
    if lst[i]<lst[i+1]:
        count+=1
    else:
        if count>max_count:
            max_count = count
        count = 1
if count>max_count:
    max_count = count
print(max_count)