import re
lst = re.findall(r'\d+',input())
lst = list(map(int,lst))

max_number = max(lst)
count = 0
pre_index = 0
i = 0
while i<= max_number:
    index = lst.index(i)
    if max(lst[pre_index:index+1])==index:
        count+=1
        pre_index = index+1
        i = index+1
    else:
        i+=1
print(count)