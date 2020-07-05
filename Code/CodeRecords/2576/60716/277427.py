def changeR(num:int):
    templist = list()
    index = 0
    for i in lists:
        if i>num:
            index+=num
        else:
            index+=i
    return abs(index-target)
strs = input().split(',')
target = int(input())
lists = [int(i) for i in strs]
simi = target//len(lists)
a = list()
b = list()
a.append(simi)
b.append(changeR(simi))
a.append(simi+1)
b.append(changeR(simi+1))
a.append(simi-1)
b.append(changeR(simi-1))
for i in range(min(lists),max(lists)+1):
    a.append(i)
    b.append(changeR(i))
uses = list(zip(a,b))
sortlist = sorted(uses,key=lambda quality:quality[1])
print(uses[0][0])