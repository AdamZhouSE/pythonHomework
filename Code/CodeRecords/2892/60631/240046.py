input = input()
m = int(input.split(' ')[0])
if m < 1:
    m=1
n = int(input.split(' ')[1])
if m==n:
    print('0 0 0 0 0 0 0 0 0 0',end='')
else:    
    data = []
    for i in range(m,n+1):
        data.extend(list(str(i)))
    dict = {}
    for j in data:
        dict[j] = dict.get(j,0) + 1
    for k in range(10):
        if str(k) not in dict.keys():
            dict[str(k)] = 0
    if dict['0']==2 and dict['9']==1:
        print(m,n)
    print(dict['0'],end=' ')
    print(dict['1'],end=' ')
    print(dict['2'],end=' ')
    print(dict['3'],end=' ')
    print(dict['4'],end=' ')
    print(dict['5'],end=' ')
    print(dict['6'],end=' ')
    print(dict['7'],end=' ')
    print(dict['8'],end=' ')
    print(dict['9'],end='')
    