def VKnum(List):
    count = 0
    for i in range(len(List) -1):
        if List[i] is 'V' and List[i + 1] is 'K':
            count = count + 1
    return count

strLen = input()
Str = input()
List = list(Str)
base = VKnum(Str)
change = 0
control = 0
for i in range(len(Str)):
    if List[i] is 'V':
        List[i] = 'K'
        change = VKnum(List)
        if change > base:
            control = 1
            print(change, end = '')
            break
        List[i] = 'V'
    else:
        List[i] = 'V'
        change = VKnum(List)
        if change > base:
            control = 1
            print(change, end = '')
            break
        List[i] = 'K'
if control == 0:
    print(base, end = '')