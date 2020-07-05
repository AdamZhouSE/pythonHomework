from itertools import permutations
a = input().split(',')
res = []
l = list(permutations(a,len(a)))
for i in l:
    hour = i[0]+i[1]
    minute = i[2]+i[3]
    if hour>'23' or minute>'59':
        pass
    else:
        time = ':'.join([hour,minute])
        if time not in res:
            res.append(time)
if res:
    res.sort(reverse=True)
    print(res[0])
else:
    print('')