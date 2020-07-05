start = str(input())
end = str(input())
if len(start) != len(end):
    print('False')
else:
    i = 0
    j = 0
    flag = 'True'
    h = 1
    while i < len(end) and j < len(end):
        while start[i] == 'X':
            i = i + 1
            if i >= len(end):
                h=0
                break
        try:
            while end[j] == 'X':
                j = j + 1
                if j >= len(end):
                    h=0
                    break
        except:
            print(start, end)
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
