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

if len(const)> 1:
    isUnimodal = False
elif len(const) == 1:
    const = const[0]
    begin = lst.index(const)
    end = lst[::-1].index(const)
    isUnimodal = up(lst[:begin+1]) and up(lst[::-1][:end+1])
else: # == 0
    maxNum = max(lst)
    index = lst.index(maxNum)
    isUnimodal = up(lst[:index+1]) and up(lst[::-1][:len(lst)-1-index])

if isUnimodal:
    print("YES")
else:
    print('NO')