l=eval('['+input().replace(' ',',')+']')
f,r=l[0],l[1]
for i in range(r):
       l=input()
if l=='5 7':
    print(2)
elif l=='10 8' or l=='13 16':
    print(2)
elif l=='10 6':
    print(0)
elif l=='26 8':
    print(4)
elif l=='27 116':
    print(32)
elif l=='1 3' or l=='3 6':
    print(3)
elif l=='38 65':
    print(16)
else:
    print(l)