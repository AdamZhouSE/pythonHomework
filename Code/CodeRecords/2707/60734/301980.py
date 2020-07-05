import re
lst = list(map(int,re.findall('\d+',input())))
#lst = [3,2,0,1]
fixed = [False]*(len(lst))
cnt = 0
while False in fixed:
    begin = fixed.index(False)
    id = lst[begin]
    if id%2 == 0:
        pair = id+1
    else:
        pair = id-1
    index = lst.index(pair)
    fixed[index] = True
    if index%2 == 0:
        pairindex = index+1
    else:
        pairindex = index-1
    if pairindex != begin:
        lst[pairindex],lst[begin] = lst[begin],lst[pairindex]
        cnt+=1
    fixed[pairindex] = True
print(cnt)