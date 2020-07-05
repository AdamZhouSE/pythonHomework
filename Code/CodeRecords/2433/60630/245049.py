a = input('')[2:-2].split('],[')

b = [[int(k) for k in a[0].split(',')]]
for i in a[1:]:
    x, y= [int(k) for k in i.split(',')]
    
    j1 = 0; j2 = len(b) - 1
    while b[j1][0] < x and b[j1][1] < x:
        j1 += 1
        if j1 >= len(b): break
    while b[j2][1] > y and b[j2][1] > y:
        j2 -= 1
        if j2 < 0: break
    if j1 in range(0, len(b)):
        if b[j1][0] < x:
            x = b[j1][0]
    if j2 in range(0, len(b)):
        if b[j2][1] > y:
            y = b[j2][0]
        
    while j2 >= j1:
        del b[j2]
        j2 -= 1
    b.insert(j1, [x, y])
    
print(b)
