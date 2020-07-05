n = int(input())
lst = input().split(' ')
lst = list(map(int,lst))

isUnimodal = True
const = []
for i in range(len(lst)-1):
    if lst[i] == lst[i+1] and lst[i] not in const:
        const.append(lst[i])

if len(const)!= 1:
    isUnimodal = False
else:
    const = const[0]
    begin = lst.index(const)
    if begin>0:
        for i in range(1,begin+1):
            if lst[i-1]>lst[i]:
                isUnimodal = False
    lst.reverse()
    end = lst.index(const)
    if end>0:
        for i in range(1,end+1):
            if lst[i-1]>lst[i]:
                isUnimodal = False
if len(lst) == 1:
    isUnimodal = True

if isUnimodal:
    print("YES")
else:
    print('NO')