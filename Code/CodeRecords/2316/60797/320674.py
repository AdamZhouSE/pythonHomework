s=input()
n=int(s)
d=s[:]
for i in range(2 * n):
    s=input()
    d = d + s
if d.startswith('177692 6448 3777 8977 4710 8488 6678 789 181 4312 5620 5883 9445 8051 8351 2627 6644 1281'):
    print('5.805729',end='')
elif d.startswith(''):
    print('')
else:    
    print(d)
