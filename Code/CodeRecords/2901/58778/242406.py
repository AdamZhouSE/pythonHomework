n=int(input())
s=bin(n)
sl=list(s)
j=1
for i in range(len(sl)-1):
    if(sl[i]==sl[i+1]):
        j=0
        break
if(j==0):
    print('False')
else:
    print('True')