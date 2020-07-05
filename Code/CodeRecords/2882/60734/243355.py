def up(lst):
    if len(lst)>1:
        for i in range(1,len(lst)):
            if(lst[i-1])>lst[i]:
                return False
    return True

n = int(input())
lst = input().split(' ')
lst = list(map(int,lst))

isUnimodal = True
const = []
for i in range(len(lst)-1):
    if lst[i] == lst[i+1] and lst[i] not in const:
        const.append(lst[i])

if len(const)!= 1:
    if len(lst) == 1:
        isUnimodal = True
    else:
        isUnimodal = False
else:
    const = const[0]
    begin = lst.index(const)
    isUnimodal = up(lst[:begin+1])
    lst.reverse()
    end = lst.index(const)
    isUnimodal = up(lst[:end+1])

if isUnimodal:
    print("YES")
else:
    print('NO')