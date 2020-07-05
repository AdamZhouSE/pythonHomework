n = eval(input())
a = ''
for i in range(n):
    order = input().split(' ')
    if order[0] == 'T':
        a = a + order[1]
    elif order[0] == 'Q':
        print(a[int(order[1])-1])
    else:
        a = a[0:len(a)-int(order[1])]
