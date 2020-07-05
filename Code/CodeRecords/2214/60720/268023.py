a=input().split('+')
b=input().split('+')
isN=False
if a[1][0]=='-':
    a[1]=a[1][1:]
    isN=True
if isN:
    a[1]=0-int(a[1][0:-1])
else:
    a[1]=int(a[1][0:-1])
isN = False
if b[1][0][0] == '-':
    b[1] = b[1][1:]
    isN = True
if isN:
    b[1] = 0 - int(b[1][0:-1])
else:
    b[1]=int(b[1][0:-1])
isN = False
if a[0][0] == '-':
    a[0] = a[0][1:]
    isN = True
if isN:
    a[0] = 0 - int(a[0])
else:
    a[0]=int(a[0])
isN = False
if b[0][0] == '-':
    b[0] = b[0][1:]
    isN = True
if isN:
    b[0] = 0 - int(b[0])
else:
    b[0]=int(b[0])
result=[0,0]
result[0]=a[0]*b[0]-a[1]*b[1]
result[1]=a[0]*b[1]+a[1]*b[0]
print('{}+{}i'.format(result[0],result[1]))
