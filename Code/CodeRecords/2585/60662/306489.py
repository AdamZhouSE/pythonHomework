start = str(input())
end = str(input())
if len(start) != len(end):
    print('False')
else:
    i = 0
    j = 0
    flag = 'True'
    h=1
    while i < len(end) and j < len(end):
        while i<len(start):
            if start[i] == 'X':
                i = i + 1
            elif i>=len(start):
                h=0
                break
            else:
                break
        while j<len(end):
            if end[j] == 'X':
                j = j + 1
            elif j>=len(end):
                h=0
                break
            else:
                break
        if h==0:
            break
        if start[i] != end[j]:
            flag = 'False'
        if start[i] == 'L' and i < j:
            flag = 'False'
        if start[i] == 'R' and i > j:
            flag = 'False'
        i += 1
        j += 1
    print(flag)