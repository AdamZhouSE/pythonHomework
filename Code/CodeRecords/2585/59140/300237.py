start = input().upper()
end = input().upper()
flag = True
if start.replace('X','') != end.replace('X',''):
    flag = False
else:
    start = list(start)
    end = list(end)
    temp = 0
    for i in range(len(start)):
        if start[i] == 'L':
            try:
                while end[temp] != 'L': temp += 1
            except:
                print(start,end)
            if i < temp: flag = False
            temp += 1
    temp = 0
    for i in range(len(start)):
        if start[i] == 'R':
            while end[temp] != 'R': temp += 1
            if i > temp: flag = False
            temp += 1
print(flag)