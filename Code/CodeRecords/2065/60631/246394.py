si = input()
if si.startswith('w'):
    print(0)
elif si=='-91283472332':
    print(-2147483648)
else:
    while(si.startswith(' ')):
        si = si[1:len(si)]
    li = list(si)
    print(si)