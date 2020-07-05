cmd = [int(i) for i in input().split( )]

while cmd[1]:
    m, n = cmd[0], cmd[1]
    t, s, summ = 1, 0, 1
    i = m
    while i<n:
        i = 2*i+1
        s += 1
    j=s-1
    while j:
        t = t*2
        summ += t
        j -= 1
    t  =t*2
    if n-m*t >= 0:
        summ = summ+n-(m*t)+1
    print(summ)
    cmd = [int(i) for i in input().split( )]
'''    
m, n = cmd[0], cmd[1]
t, s, summ = 1, 0, 1
i = m
while i<n:
    i = 2*i+1
    s += 1
j=s-1
while j:
    t = t*2
    summ += t
    j -= 1
t = t*2
if n-m*t >= 0:
    summ = summ+n-(m*t)+1
print(summ)   
'''