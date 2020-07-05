s = str(input())
length = len(s)
order = str(input()).split(' ')

if '' in order:
    for i in order:
        if i == '':
            order.remove('')
                                  
if order[0] == 'D':
    s=s.replace(str(order[1]), '',1)
    if len(s) == length:
        print('no exist')
        print(s)
    else:
        print(s)
elif order[0] == 'I':
    letters = list(s)
    k = len(s) - 1
    flag = 0
    while k >= 0:
        if letters[k] == order[1]:
            letters[k] = order[2] + order[1]
            flag = 1
            break
        k -= 1
    if flag == 0:
        print('no exist')
        print(s)
    else:
        print(''.join(letters))
elif order[0] == 'R':
    temp = s.replace(order[1], order[2])
    if temp == s:
        print('no exist')
        print(s)
    else:
        print(temp)

