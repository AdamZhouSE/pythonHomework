input()

a = input().split()
b = []

for i in range(len(a)):
    if( b.count(int(a[i]))==0 ):
        b.append(int(a[i]))
b.sort()

if( len(b)==1 ):
    print(0)
elif( len(b)==2 ):
    print(b[1]-b[0])
elif( len(b)==3 and b[2]-b[1]==b[1]-b[0]):
    if(b[2]-b[1]==6):
        print(b)
    print(b[2]-b[1])
else:
    print(-1)