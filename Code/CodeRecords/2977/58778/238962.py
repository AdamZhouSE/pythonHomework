strlist=[]
while True:
    s=input()
    if(s=='!'):
        break
    strlist.append(s)
strup='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
strlow='abcdefghijklmnopqrstuvwxyz'
listup=list(strup)
listlow=list(strlow)
listup.reverse()
listlow.reverse()

for i in strlist:
    for r in range(len(i)):
        if ord(i[r:r+1])>=ord('a') and ord(i[r:r+1])<=ord('z'):
            print(listlow[ord(i[r:r+1])-ord('a')],end='')
        elif ord(i[r:r+1])>=65 and ord(i[r:r+1])<=ord('Z'):
            print(listup[ord(i[r:r+1])-65],end='')
        else:
            print(i[r:r+1],end='')
    print('')